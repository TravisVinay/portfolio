---
name: quiz-me
description: Interactively quiz the user on their notes, a study guide, or a topic, one question at a time, adapting to weak spots and tracking results across sessions. Use when the user wants to be quizzed, tested, or drilled.
argument-hint: '<file, folder, or topic> [number of questions] [easy|medium|hard|mixed]'
---

# Quiz me

Quiz the user on: **$ARGUMENTS**

## 1. Set up

- Read the source material (a file, folder, `*-study-guide.md`, or files attached to the chat) the same way you'd read notes: all of it, including every page of a PDF. For a bare topic with no file, quiz from general knowledge at an intro-course level unless told otherwise.
- **Defaults:** 10 questions, `mixed` difficulty. The arguments can override both (e.g. `notes.pdf 5 hard`).
- **Check history:** look for past results in either of these places:
  - a `quiz-results.md` file in the same folder as the source (or in the current directory if the source was a topic), or
  - a **progress note** the user pasted or attached in the chat (a block that starts with `QUIZ PROGRESS NOTE`).

  If you find either, read the most recent entries for this topic and put more questions on the concepts listed as weak there, about half the quiz.
- Tell the user in one line what you're quizzing on, how many questions there are, and what you're focusing on (e.g. "focusing on X and Y, which you missed last time"). Then ask question 1 right away.

## 2. Ask one question at a time

**Ask exactly one question, then stop and wait for the answer.** Never put two questions in one message, and never reveal an answer before the user tries.

Mix the question types:
- Short answer / explain in your own words
- Multiple choice (4 options with plausible wrong answers, labeled A–D)
- Apply it: a scenario, calculation, or "what would happen if…"
- Compare / contrast two concepts
- Spot the error in a statement

Format each question as `**Q3/10** · <concept>` followed by the question.

The user can type at any time:
- `hint`: give a nudge without giving the answer (counts as half credit if they then get it right)
- `skip` / `idk`: show the answer, explain it, and mark the question missed
- `stop`: end the quiz early and go straight to the results
- `harder` / `easier`: change the difficulty from the next question onward

## 3. Grade each answer

After each answer:
1. Give a verdict: ✅ Correct, 🟡 Partly, or ❌ Not quite.
2. Explain in 1–3 sentences why. On 🟡 or ❌, give the correct answer and the key idea they missed, and tie it back to the notes when you can (e.g. "your lecture 4 notes define it as…").
3. Grade on understanding, not wording. A paraphrase that captures the idea counts as correct, and small typos don't matter.
4. Then ask the next question in the same message.

**Adapt as you go:** if they miss a concept, ask about it again later from a different angle. If they get three in a row right, make the questions harder.

## 4. Results

When the quiz ends, show:
- The score (e.g. 7.5 / 10)
- ✅ **Strong:** the concepts they clearly know
- ⚠️ **Review:** the concepts they missed or were shaky on, each with a one-line reminder of the key idea
- One concrete suggestion for what to study next

Then save the results so the next quiz can focus on weak spots. Use this entry format:

```markdown
## <date> · <topic / source file> · <score>/<total> · <difficulty>
- Weak: <concept>, <concept>
- Strong: <concept>, <concept>
- Missed: <one short line per missed question>
```

**If the notes are files on the user's computer** (for example, in Claude Code): append the entry to `quiz-results.md` next to the source, creating the file if it doesn't exist. Tell the user the results were saved and that the next quiz will focus on their weak spots.

**Otherwise** (the notes were attached to a chat, as on claude.ai, or you can't save files that will still be there next time): don't write a file. Instead, end with a progress note in a code block so it's easy to copy. Include the new entry plus the entries from any note they pasted at the start, keeping the 5 most recent:

```
QUIZ PROGRESS NOTE: paste this at the start of your next quiz
<entries, newest first>
```

Tell the user to save the note somewhere (a notes app or a text file) and paste it in, along with their notes, the next time they ask to be quizzed, so the quiz can focus on what they missed.
