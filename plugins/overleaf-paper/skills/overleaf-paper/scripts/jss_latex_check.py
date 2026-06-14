#!/usr/bin/env python3
"""Lightweight JSS LaTeX manuscript checks.

This script is intentionally conservative. It reports likely issues; it does not
try to fully parse LaTeX.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        escaped = False
        out = []
        for ch in line:
            if ch == "\\" and not escaped:
                escaped = True
                out.append(ch)
                continue
            if ch == "%" and not escaped:
                break
            escaped = False
            out.append(ch)
        lines.append("".join(out))
    return "\n".join(lines)


def brace_arg(command: str, text: str) -> list[str]:
    pattern = re.compile(r"\\" + re.escape(command) + r"\s*\{")
    values = []
    for match in pattern.finditer(text):
        start = match.end()
        depth = 1
        i = start
        while i < len(text) and depth:
            if text[i] == "{" and (i == 0 or text[i - 1] != "\\"):
                depth += 1
            elif text[i] == "}" and (i == 0 or text[i - 1] != "\\"):
                depth -= 1
            i += 1
        if depth == 0:
            values.append(text[start : i - 1].strip())
    return values


def split_keywords(raw: str) -> list[str]:
    raw = raw.replace("\\sep", ",")
    return [item.strip() for item in re.split(r"[,;]", raw) if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tex", type=Path, help="Path to the main .tex file")
    args = parser.parse_args()

    text = strip_comments(args.tex.read_text(encoding="utf-8", errors="replace"))
    issues: list[str] = []
    warnings: list[str] = []

    highlights = brace_arg("highlights", text)
    if highlights:
        items = re.findall(r"\\item\s+(.+?)(?=\\item|\\end\{highlights\}|$)", highlights[0], re.S)
        cleaned = [re.sub(r"\s+", " ", item).strip() for item in items]
        if not 3 <= len(cleaned) <= 5:
            issues.append(f"Highlights count is {len(cleaned)}; JSS expects 3 to 5.")
        for idx, item in enumerate(cleaned, 1):
            plain = re.sub(r"\\[a-zA-Z]+\*?(\[[^]]*\])?(\{[^}]*\})?", "", item)
            if len(plain) > 85:
                issues.append(f"Highlight {idx} is {len(plain)} characters; maximum is 85.")
    else:
        warnings.append("No highlights environment or command found.")

    keyword_blocks = brace_arg("begin{keyword}", text) or brace_arg("keywords", text)
    if keyword_blocks:
        keywords = split_keywords(keyword_blocks[0])
        if not 1 <= len(keywords) <= 7:
            issues.append(f"Keyword count is {len(keywords)}; JSS expects 1 to 7.")
    else:
        warnings.append("No keyword block found.")

    if re.search(r"\\section\*?\s*\{\s*Abstract\s*\}", text, re.I):
        issues.append("Abstract appears as a section; JSS expects an unnumbered abstract block.")

    for env in ["figure", "table"]:
        labels = re.findall(r"\\begin\{" + env + r"\}.*?\\label\{([^}]+)\}.*?\\end\{" + env + r"\}", text, re.S)
        for label in labels:
            if not re.search(r"\\(ref|autoref|cref|Cref)\{" + re.escape(label) + r"\}", text):
                warnings.append(f"{env.title()} label '{label}' may not be cited in text.")

    if re.search(r"\\bibliography\{|\\begin\{thebibliography\}", text) and re.search(r"\\section\*?\s*\{\s*Acknowledg", text, re.I):
        ack_pos = re.search(r"\\section\*?\s*\{\s*Acknowledg", text, re.I).start()
        bib_match = re.search(r"\\bibliography\{|\\begin\{thebibliography\}", text)
        if bib_match and ack_pos > bib_match.start():
            issues.append("Acknowledgements appear after references; place them before references.")

    print("JSS LaTeX check")
    print(f"File: {args.tex}")
    if issues:
        print("\nIssues:")
        for issue in issues:
            print(f"- {issue}")
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    if not issues and not warnings:
        print("No issues found by lightweight checks.")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
