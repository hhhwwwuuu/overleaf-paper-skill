# Journal of Systems and Software Offline Writing And Formatting Reference

Use this file as the offline checklist for Journal of Systems and Software (JSS) manuscript work. The source link is retained at the end, but the agent should not need network access for routine writing and formatting decisions.

## Journal Fit

JSS publishes work across software engineering. Manuscripts should support claims with evidence such as empirical studies, simulations, formal proofs, experiments, validations, or other clearly described methods. When revising, make sure the paper does not make unsupported claims.

## File Format And Source Files

- Use editable source files.
- For LaTeX submissions, use an Elsevier-compatible LaTeX template when possible.
- Keep the main manuscript source compilable.
- Do not represent equations, tables, or text as images when they can be editable source.
- Keep figures, tables, bibliography, and supplementary material in clearly named files.
- Avoid committing generated LaTeX build files unless explicitly required by the submission package.

## Title Page Checklist

Check that the manuscript has or can provide:

- Concise, informative title.
- Author names.
- Author affiliations.
- Corresponding author details.
- Present/permanent address notes when needed.
- Funding, competing interest, AI-use, data availability, and contribution statements when required by the submission system.

Do not invent author metadata, funding, ethics, conflicts, AI-use declarations, data availability, or CRediT roles. Ask the user when information is missing.

## Abstract

- Keep the abstract self-contained.
- Do not number the abstract as a section.
- Avoid undefined abbreviations.
- Avoid citations unless necessary; if a citation is used in the abstract, ensure full reference information exists in the reference list.
- State problem, method, evidence, result, and implication at a high level.

## Keywords

- Provide 1 to 7 keywords.
- Use English keywords.
- Prefer specific terms readers would search for.
- Avoid duplicating only words already in the title unless they are essential search terms.

## Highlights

- Provide 3 to 5 highlights.
- Each highlight must be at most 85 characters including spaces.
- Use concrete findings, contributions, or evidence statements.
- Avoid vague process statements such as "A method is proposed" without substance.
- Keep highlights understandable outside the full paper.

Example shape:

```text
Highlights
- <concrete contribution or finding under 85 characters>
- <method or dataset contribution under 85 characters>
- <result, implication, or reproducibility point under 85 characters>
```

## Graphical Abstract

If provided:

- Use it to summarize the main finding or workflow visually.
- Ensure it is clear without relying on the full manuscript.
- Do not use generative AI to create artwork for graphical abstracts.

## Generative AI Disclosure

- If generative AI or AI-assisted tools were used in manuscript writing, follow the journal/submission disclosure requirement.
- Do not list AI tools as authors.
- If AI tools are part of the research method itself, describe the tool/model/version and usage in a reproducible way in the methods section.
- Do not use generative AI to create or alter scientific artwork unless the journal explicitly permits the specific use case.

## Article Structure

- Divide the article into clearly defined numbered sections.
- Number subsections as `1.1`, `1.1.1`, `1.1.2`, `1.2`, etc.
- Use section numbering when cross-referencing; do not write vague references such as "the text above".
- Give subsections brief headings on separate lines.
- Do not include the abstract in section numbering.

A typical empirical software engineering paper can use:

```text
1. Introduction
2. Background and Related Work
3. Methodology
4. Results
5. Discussion
6. Threats to Validity
7. Conclusion
```

Adapt the structure to the study type; do not force this exact outline if the manuscript has a better established structure.

## Acknowledgements

- Put acknowledgements in a separate section directly before the reference list.
- Do not place acknowledgements on the title page.
- Do not make acknowledgements a footnote to the title.
- Include language, writing, proof-reading, technical, or research help when appropriate.

## Author Contributions: CRediT

Corresponding authors must acknowledge co-author contributions using relevant CRediT roles. Use only roles that apply:

- Conceptualization
- Data curation
- Formal analysis
- Funding acquisition
- Investigation
- Methodology
- Project administration
- Resources
- Software
- Supervision
- Validation
- Visualization
- Writing - original draft
- Writing - review and editing

Authors may have multiple roles. Ask the user for contribution details instead of guessing.

## Appendices

- Label appendices as Appendix A, Appendix B, etc.
- Number equations separately in appendices, e.g. Eq. (A.1), Eq. (A.2), Eq. (B.1).
- Number appendix tables and figures separately, e.g. Table A.1, Fig. A.1.

## Vitae

If biographies are requested, prepare a short editable biography for each author. Maximum length is 100 words per author.

## Manuscript Length

- Full-length papers are encouraged to stay below 36 single-column pages or 18 double-column pages.
- If longer, prepare a justification for the submission.
- Review articles have no fixed page count, but the length should be justified by the content.

## Math Formulae And Equations

- Keep formulae editable as text/LaTeX.
- Number displayed equations when referenced.
- Define symbols and variables near first use.
- Avoid embedding equations as images.

## Tables

- Cite every table in the manuscript text.
- Number tables consecutively in order of appearance.
- Provide concise titles/captions.
- Keep tables editable, not screenshots.
- Avoid vertical rules and unnecessary shading.
- Define abbreviations, symbols, and statistical notation in the caption or table notes.
- Ensure table data support the claims in the surrounding text.

## Figures, Images, And Artwork

- Cite every figure in the manuscript text.
- Number figures consecutively in order of appearance.
- Provide captions that explain symbols, abbreviations, labels, and key visual encodings.
- Ensure image files are clearly named and linked from the manuscript.
- Do not manipulate images in a misleading way.
- Do not use generative AI to produce scientific artwork unless explicitly permitted for the use case.

## Supplementary Material

- Cite all supplementary files in the manuscript text.
- Submit supplementary files with the manuscript.
- Give each supplementary file a concise descriptive caption.
- Ensure supplementary material is accurate and relevant.
- Remember supplementary files may appear online as provided and may not be copyedited or typeset.

## Video Or Animation

If video/animation is used:

- Refer to it in the manuscript where it should appear.
- Use file names that describe the content.
- Provide still images when required.
- Provide descriptive text for accessibility.
- Keep within the journal's file size expectations when known.

## Research Data And Data Statement

JSS requires a data availability statement at submission.

For research data:

- Deposit research data in a relevant repository when possible.
- Cite and link the dataset in the article.
- If data cannot be shared, state the reason clearly.
- Research data may include observations, experimental results, software, code, models, algorithms, protocols, methods, or other materials needed to validate findings.

Do not invent repository links or availability claims. Ask the user if data status is unclear.

## Data Linking

If data are available in a repository:

- Provide the dataset link during submission.
- Link relevant identifiers in the manuscript text where appropriate.
- Use stable identifiers when available, such as DOI or repository accession IDs.

## References In Text

- Every in-text citation should appear in the reference list.
- Every reference-list item should be cited in the manuscript, unless the chosen style explicitly allows otherwise.
- Citations in the abstract must have full reference information.
- Avoid unpublished results and personal communications in the reference list when possible.
- If unpublished or personal communications are included, label them according to journal style.
- "In press" should only be used for accepted works.
- Check author names, titles, year, venue, volume, article number, pages, and DOI before submission.

## Reference Format

- JSS does not require a strict reference style at initial submission.
- Use one consistent style throughout the manuscript.
- Include author names, title, year, journal/book/conference title, volume, article number or pages where applicable.
- Use DOIs when available.
- Expect the publisher to apply journal reference style at proof stage and ask for missing data if needed.

## Offline Agent Checklist For JSS Review

When asked to check or revise a JSS manuscript, inspect:

1. Title page metadata completeness.
2. Abstract is unnumbered and self-contained.
3. Keywords count is 1 to 7.
4. Highlights count is 3 to 5 and each is under 85 characters.
5. Main sections and subsections are numbered.
6. Acknowledgements appear immediately before references if present.
7. CRediT contribution statement exists or missing information is flagged.
8. Tables and figures are cited, numbered, editable where applicable, and captioned.
9. Equations are editable and symbols are defined.
10. Supplementary material is cited and captioned.
11. Data availability statement exists.
12. References are consistent and citation/reference lists match.
13. Manuscript length is flagged if above 36 single-column or 18 double-column pages.
14. AI-use, funding, competing interest, and ethics statements are not invented.

## Sources

- https://www.sciencedirect.com/journal/journal-of-systems-and-software/publish/guide-for-authors