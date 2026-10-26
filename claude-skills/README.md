# Study Skills for Claude Code

Two slash commands that turn your class notes into study material and then quiz you on it. The examples below use the short names. If you installed the plugin, type `/study-skills:study-guide` and `/study-skills:quiz-me` instead (see [Installation](#installation)).

| Command | What it does |
|---------|--------------|
| `/study-guide` | Turns notes, slides, or readings into a structured, exam-ready study guide saved as Markdown. |
| `/quiz-me` | Quizzes you one question at a time, grades your answers, and remembers your weak spots between sessions. |

They work well together:

```
/study-guide lecture5.pdf          →  creates lecture5-study-guide.md
/quiz-me lecture5-study-guide.md   →  quizzes you on it, saves results to quiz-results.md
/quiz-me lecture5-study-guide.md   →  next time, focuses on what you missed
```

---

## Installation

### As a plugin (recommended)

In Claude Code, run:

```
/plugin marketplace add TravisVinay/portfolio
/plugin install study-skills@travisvinay
```

On Claude Code 2.1.275 or later, one line does both:

```
/plugin install study-skills --marketplace TravisVinay/portfolio
```

From a terminal instead:

```bash
claude plugin marketplace add TravisVinay/portfolio
claude plugin install study-skills@travisvinay
```

Plugin skills are namespaced, so the commands are **`/study-skills:study-guide`** and **`/study-skills:quiz-me`**. You can also just ask ("make a study guide from lecture5.pdf", "quiz me on my notes") and Claude will use them. To get updates later, run `/plugin marketplace update travisvinay`.

### Manually (shorter command names)

Copy the two folders from [`skills/`](skills) into `~/.claude/skills/` (on Windows, `C:\Users\<you>\.claude\skills\`), or into `<project>/.claude/skills/` for one project only. Then start a new Claude Code session. This way the commands are plain `/study-guide` and `/quiz-me`, but you won't get updates automatically.

### On claude.ai (browser or Claude app)

The skills also work in regular Claude chat, without Claude Code:

1. Download the zips: [study-guide.zip](https://github.com/TravisVinay/portfolio/raw/main/claude-skills/downloads/study-guide.zip) and [quiz-me.zip](https://github.com/TravisVinay/portfolio/raw/main/claude-skills/downloads/quiz-me.zip).
2. On claude.ai, open **Settings → Capabilities**, find **Skills**, and upload each zip. Code execution needs to be turned on.
3. In a chat, attach your notes and ask: *"Make a study guide from these notes"* or *"Quiz me on this, 10 questions, hard."*

How it differs from Claude Code:
- There are no slash commands. Just ask, and Claude uses the skill when your request matches.
- The study guide comes back as a file to download.
- Each chat starts fresh, so the quiz can't save `quiz-results.md` between chats. Instead it ends with a **QUIZ PROGRESS NOTE**. Save that text somewhere, and paste it in with your notes next time so the quiz focuses on what you missed.

### Optional

Reading `.pptx` and `.docx` files needs `pip install python-pptx python-docx`. PDFs, Markdown, and text files need nothing extra.

### Plugin layout

```
portfolio/
├── .claude-plugin/
│   └── marketplace.json      # lists the study-skills plugin
└── claude-skills/            # the plugin
    ├── .claude-plugin/
    │   └── plugin.json
    ├── README.md
    ├── skills/
    │   ├── study-guide/SKILL.md
    │   └── quiz-me/SKILL.md
    ├── downloads/            # zips for claude.ai upload
    └── build-zips.py         # rebuilds the zips after edits
```

---

## `/study-guide`

```
/study-guide <file, folder, or topic> [focus]
```

**Examples**
```
/study-guide lecture5.pdf
/study-guide "CSE 373 notes"                 # a whole folder of notes
/study-guide notes.pdf midterm 2 only        # restrict to a focus
/study-guide photosynthesis                  # no notes: uses general knowledge
```

**Accepts:** PDF, PowerPoint, Word, Markdown, text, or code files, a folder of notes, or just a topic name.

**Output:** a file named `<source>-study-guide.md`, saved next to your notes. It contains:

- **The big picture:** what the material is about and how it fits together
- **Key concepts:** plain-English explanations with examples
- **Terms to know:** a table of definitions, with a *"don't confuse with"* column
- **Formulas / processes:** with every symbol and step explained
- **How it connects:** the relationships between concepts
- **Common mistakes:** the traps students fall into
- **Likely exam questions:** ordered easy → hard
- **Practice problems:** questions that make you apply the material
- **Answer key:** kept separate so you can test yourself first
- **Self-check:** an "I can…" checklist

**Behavior notes**
- It sticks to your course's own terms, notation, and examples, and doesn't add material your notes don't cover.
- Anything in your notes that looks wrong or unclear is marked **⚠️ Check this** rather than silently changed.
- Before overwriting an existing study guide, it asks first.

---

## `/quiz-me`

```
/quiz-me <file, folder, or topic> [number of questions] [easy|medium|hard|mixed]
```

**Examples**
```
/quiz-me lecture5-study-guide.md
/quiz-me notes.pdf 5 hard
/quiz-me "cell biology" 15
```

The defaults are **10 questions** at **mixed** difficulty.

**How it works**
1. It asks **one question at a time** and waits for your answer.
2. The question types vary: short answer, multiple choice, apply-it scenarios, compare/contrast, and spot-the-error.
3. Each answer gets ✅ Correct / 🟡 Partly / ❌ Not quite, with a short explanation tied back to your notes.
4. Grading is on understanding, not exact wording. Paraphrasing and small typos are fine.
5. It adapts as you go: missed concepts come back later from a different angle, and a streak of right answers makes the questions harder.

**Commands during a quiz**

| Type | Effect |
|------|--------|
| `hint` | A nudge without the answer (half credit if you then get it right) |
| `skip` / `idk` | Shows and explains the answer (counts as missed) |
| `harder` / `easier` | Changes difficulty from the next question on |
| `stop` | Ends early and shows your results |

**Results and progress tracking**

At the end you get a score, a list of strong and weak concepts, and a suggestion for what to study next. Each session is also appended to `quiz-results.md` next to your notes:

```markdown
## 2026-10-22 · lecture5-study-guide.md · 7.5/10 · mixed
- Weak: Dijkstra's algorithm, heap invariants
- Strong: BFS vs DFS, big-O of hash tables
- Missed: Why Dijkstra fails with negative edges
```

The next time you run `/quiz-me` on the same material, it reads this file and puts about half the questions on your weak spots.

On claude.ai, where files don't carry over between chats, the quiz prints the same entries as a **QUIZ PROGRESS NOTE** for you to copy. Paste it in at the start of your next quiz to get the same focus on weak spots.

---

## Customizing

Each skill is a plain Markdown file of instructions, so you can change its behavior by editing it:

- **Change the study guide layout:** edit the template in `skills/study-guide/SKILL.md` (step 2).
- **Change quiz defaults** (question count, difficulty, question types): edit `skills/quiz-me/SKILL.md` (steps 1–2).
- **Make grading stricter or looser:** edit the "Grade each answer" section in `skills/quiz-me/SKILL.md`.

After editing, run `python claude-skills/build-zips.py` so the claude.ai zips match, and raise `"version"` in `.claude-plugin/plugin.json` so plugin users get the update.

---

## Limitations

- The guides and quizzes are only as good as your notes. Check anything that looks off against the textbook or lecture.
- With a bare topic and no notes, everything comes from Claude's general knowledge, which might not match how your course teaches it.
- Scanned or handwritten PDFs may not read well. Typed notes work best.
- The progress tracking is per folder: `quiz-results.md` lives next to the notes you quizzed on. On claude.ai it only carries over if you paste in your progress note.
