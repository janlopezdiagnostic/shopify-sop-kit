# Start here

Five minutes to set up. The kit is plain markdown files, so every path below ends at
the same place: your assistant has the SOP Writer rules, the interview, and
one workflow module, and you answer questions in your own words.

## The universal path (works in any AI assistant)

1. Download the kit ZIP from the Releases page, or copy the files from this
   repo.
2. In a new chat, upload four files: `skill/SKILL.md`,
   `skill/interview.md`, the module for your task from `modules/`, and
   `templates/follow-it-cold-checklist.md`.
3. Paste the starter prompt from `prompt.md`.
4. Answer the interview like you are explaining the job to a new associate.
   Short answers are fine. "I don't know" is a valid answer. It stays marked
   [TO CONFIRM] instead of being guessed, unless you are designing a new
   process, in which case it triggers a proposed default for your approval.
5. When you get a draft, do not just read it. Hand it to someone who did not
   write it and have them follow it on a real task
   (`templates/follow-it-cold-checklist.md`). Fix what breaks.

No file uploads available? Paste the full text of `prompt.md` instead. It
carries the core rules on its own. The modules add the Shopify detail.

## Claude

- Best: create a Project, add the kit files to the project, and chat inside
  it. Or install the SOP Writer as a Skill from
  `shopify-sop-writer-skill.zip` on the Releases page (needs a plan with
  Skills enabled).
- Optional: if a Shopify connector is available in your Claude plan and
  your workplace allows connecting it, and it can be scoped to read-only,
  it can check real products, orders, and inventory while you draft. The
  kit works fully without it, and the SOP Writer never writes to a live
  store either way.

## ChatGPT

- Create a Project and add the kit files, then start the SOP chat inside it.
  Or upload the same files directly in a normal chat.
- A Custom GPT also works (paid plans): paste the body of `skill/SKILL.md`,
  below its frontmatter block, as the GPT's instructions, and add the
  interview, module, and follow-it-cold checklist files as knowledge files.

## Gemini

- Create a Gem: paste the body of `skill/SKILL.md`, below its frontmatter
  block, as the Gem's instructions, and add the interview, module, and
  follow-it-cold checklist files as its knowledge. Or upload the files in a
  normal chat and paste the starter prompt.

## Coding assistants and agents (Cursor, Copilot, Claude Code, others)

- Point the tool at this repo. `AGENTS.md` at the root tells the tool which
  files to read and the constraints to work under. `CLAUDE.md` points to it
  for tools that look for that filename instead.

## Privacy

Do not paste customer data, order exports with customer details, or anything
your workplace has not cleared for use in an AI tool. Rough notes in your own
words, with invented example data, are enough for the interview.
