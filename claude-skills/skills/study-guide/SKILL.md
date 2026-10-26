---
name: study-guide
description: Turn lecture notes, slides, readings, or a topic into an exam-ready study guide saved as a Markdown file. Use when the user asks for a study guide, review sheet, or exam prep from their notes.
argument-hint: '<file, folder, or topic> [focus, e.g. "midterm 2" or "chapters 3-5"]'
---

# Study guide

Make a study guide from: **$ARGUMENTS**

## 1. Gather the material

- If the arguments name a **file** (PDF, .md, .txt, .docx, .pptx, code), or the user attached files to the chat, read them all. For a long PDF, read it in page ranges until you've covered everything.
- If they name a **folder**, list it and read every notes-like file in it (skip binaries and build output).
- `.pptx` / `.docx`: extract the text with a short Python script (`python-pptx` / `python-docx`). If those libraries are missing, ask the user to export the file as a PDF instead of guessing what's in it.
- If the arguments are just a **topic** with no file, ask the user once whether they have notes for it. If they don't, write the guide from general knowledge and say so at the top.
- If the arguments include a focus (e.g. "midterm 2", "chapters 3-5", "only the stats part"), cover only that part.
- If nothing was given, ask what to make a guide from.

Stay faithful to the source. Use the course's own terms, notation, and examples, and don't add advanced material the notes never mention. If something in the notes looks wrong or unclear, point it out in a "⚠️ Check this" note. Don't silently fix it.

## 2. Write the guide

Use this structure. Drop any section that has nothing in it (e.g. no formulas in a history class).

```markdown
# Study Guide: <topic>
*Source: <files> · Made <date>*

## The big picture
3–5 sentences: what this material is about and how the pieces fit together.

## Key concepts
For each major concept: a plain-English explanation (2–4 sentences),
why it matters, and one concrete example — from the notes if possible.

## Terms to know
| Term | Definition | Don't confuse with |
|------|-----------|--------------------|

## Formulas / processes / timelines
Each with what every symbol or step means and when to use it.

## How it connects
Bullet list of relationships between concepts (cause→effect, X is a special case of Y, etc.).

## Common mistakes
Specific traps students fall into on this material.

## Likely exam questions
8–12 questions, mixed types (definition, explain, compare, apply, calculate if relevant),
ordered easy → hard. No answers here.

## Practice problems
3–6 problems that make you *apply* the material, not just recall it.

## Answer key
Answers to the exam questions and practice problems, with brief reasoning.

## Self-check
A checklist of "I can…" statements, one per key concept.
```

Make it scannable: short paragraphs, bold the key words, no filler. Length should match the material. One lecture gets a page or two, a whole unit gets more.

## 3. Save and report

- Save it as `<source-name>-study-guide.md` next to the source file. If the source was a folder, save it inside that folder. If the source was only a topic, save it in the current working directory.
- If the notes were attached to a chat rather than read from the user's computer (as on claude.ai), create `<source-name>-study-guide.md` as a file the user can download instead.
- If a file with that name already exists, ask before overwriting it.
- In chat, give the file path, list the sections that are in it, and point out anything flagged with ⚠️. Mention that `/quiz-me <that file>` will quiz them on it.
