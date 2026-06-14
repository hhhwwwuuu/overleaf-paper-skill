import { spawn } from "node:child_process";
import { mkdtemp, writeFile, chmod, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema, } from "@modelcontextprotocol/sdk/types.js";
const server = new Server({ name: "overleaf-git", version: "0.1.0" }, { capabilities: { tools: {} } });
const tools = [
    {
        name: "overleaf_clone",
        description: "Clone an Overleaf Git project into a local directory. Uses OVERLEAF_GIT_TOKEN when set.",
        inputSchema: {
            type: "object",
            properties: {
                project_git_url: { type: "string" },
                local_dir: { type: "string" },
            },
            required: ["project_git_url", "local_dir"],
        },
    },
    {
        name: "overleaf_pull",
        description: "Pull the latest changes from an existing Overleaf Git clone.",
        inputSchema: dirSchema(),
    },
    {
        name: "overleaf_status",
        description: "Show git status for an Overleaf Git clone.",
        inputSchema: dirSchema(),
    },
    {
        name: "overleaf_commit",
        description: "Commit local manuscript changes in an Overleaf Git clone.",
        inputSchema: {
            type: "object",
            properties: {
                local_dir: { type: "string" },
                message: { type: "string" },
            },
            required: ["local_dir", "message"],
        },
    },
    {
        name: "overleaf_push",
        description: "Push committed changes to the Overleaf Git remote. Default branch is master.",
        inputSchema: {
            type: "object",
            properties: {
                local_dir: { type: "string" },
                remote: { type: "string", default: "origin" },
                branch: { type: "string", default: "master" },
            },
            required: ["local_dir"],
        },
    },
    {
        name: "overleaf_sync",
        description: "Run status, pull, add all, commit, and push for an Overleaf clone.",
        inputSchema: {
            type: "object",
            properties: {
                local_dir: { type: "string" },
                message: { type: "string" },
                remote: { type: "string", default: "origin" },
                branch: { type: "string", default: "master" },
            },
            required: ["local_dir", "message"],
        },
    },
];
function dirSchema() {
    return {
        type: "object",
        properties: { local_dir: { type: "string" } },
        required: ["local_dir"],
    };
}
function text(content) {
    return { content: [{ type: "text", text: content }] };
}
function requireString(args, key) {
    const value = args[key];
    if (typeof value !== "string" || value.trim() === "") {
        throw new Error(`Missing required string argument: ${key}`);
    }
    return value;
}
async function withGitAuthEnv() {
    const token = process.env.OVERLEAF_GIT_TOKEN;
    if (!token) {
        return { env: { ...process.env }, cleanup: async () => { } };
    }
    const dir = await mkdtemp(join(tmpdir(), "overleaf-git-askpass-"));
    const isWindows = process.platform === "win32";
    const askpass = join(dir, isWindows ? "askpass.cmd" : "askpass.sh");
    const script = isWindows
        ? `@echo off\r\necho %1 | findstr /i username >nul\r\nif %errorlevel%==0 (echo git) else (echo %GIT_ASKPASS_VALUE%)\r\n`
        : `#!/usr/bin/env sh\ncase "$1" in\n  *Username*|*username*) printf '%s\\n' git ;;\n  *) printf '%s\\n' "$GIT_ASKPASS_VALUE" ;;\nesac\n`;
    await writeFile(askpass, script, { encoding: "utf8" });
    if (!isWindows)
        await chmod(askpass, 0o700);
    return {
        env: {
            ...process.env,
            GIT_ASKPASS: askpass,
            GIT_ASKPASS_VALUE: token,
            GIT_TERMINAL_PROMPT: "0",
        },
        cleanup: async () => {
            await rm(dir, { recursive: true, force: true });
        },
    };
}
async function runGit(args, cwd) {
    const auth = await withGitAuthEnv();
    try {
        return await new Promise((resolvePromise, reject) => {
            const child = spawn("git", args, {
                cwd: cwd ? resolve(cwd) : undefined,
                env: auth.env,
                shell: false,
            });
            let stdout = "";
            let stderr = "";
            const timer = setTimeout(() => {
                child.kill("SIGKILL");
                reject(new Error("git command timed out"));
            }, 120000);
            child.stdout.on("data", (data) => (stdout += data.toString()));
            child.stderr.on("data", (data) => (stderr += data.toString()));
            child.on("error", reject);
            child.on("close", (code) => {
                clearTimeout(timer);
                const output = [stdout.trim(), stderr.trim()].filter(Boolean).join("\n");
                if (code === 0)
                    resolvePromise(output || "OK");
                else
                    reject(new Error(output || `git exited with code ${code}`));
            });
        });
    }
    finally {
        await auth.cleanup();
    }
}
server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools }));
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const args = (request.params.arguments ?? {});
    const name = request.params.name;
    try {
        if (name === "overleaf_clone") {
            const url = requireString(args, "project_git_url");
            const localDir = requireString(args, "local_dir");
            return text(await runGit(["clone", url, localDir]));
        }
        if (name === "overleaf_pull") {
            return text(await runGit(["pull", "--ff-only"], requireString(args, "local_dir")));
        }
        if (name === "overleaf_status") {
            return text(await runGit(["status", "--short", "--branch"], requireString(args, "local_dir")));
        }
        if (name === "overleaf_commit") {
            const localDir = requireString(args, "local_dir");
            const message = requireString(args, "message");
            await runGit(["add", "-A"], localDir);
            return text(await runGit(["commit", "-m", message], localDir));
        }
        if (name === "overleaf_push") {
            const localDir = requireString(args, "local_dir");
            const remote = typeof args.remote === "string" ? args.remote : "origin";
            const branch = typeof args.branch === "string" ? args.branch : "master";
            return text(await runGit(["push", remote, branch], localDir));
        }
        if (name === "overleaf_sync") {
            const localDir = requireString(args, "local_dir");
            const message = requireString(args, "message");
            const remote = typeof args.remote === "string" ? args.remote : "origin";
            const branch = typeof args.branch === "string" ? args.branch : "master";
            const outputs = [];
            outputs.push("status before:\n" + await runGit(["status", "--short", "--branch"], localDir));
            outputs.push("pull:\n" + await runGit(["pull", "--ff-only"], localDir));
            outputs.push("add:\n" + await runGit(["add", "-A"], localDir));
            outputs.push("commit:\n" + await runGit(["commit", "-m", message], localDir));
            outputs.push("push:\n" + await runGit(["push", remote, branch], localDir));
            return text(outputs.join("\n\n"));
        }
        throw new Error(`Unknown tool: ${name}`);
    }
    catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        return text(`ERROR: ${message}`);
    }
});
await server.connect(new StdioServerTransport());
