# CarryChapter

Pick up where someone else left off. CarryChapter is an open-source AI skill that turns selected contributions from separate AI conversations into shared notes, decisions, and open questions.

Use one Google Doc as the shared source, or use a Markdown file. Everyone keeps their own chat. CarryChapter uses the AI client's existing tools to read the source, preview a contribution, and apply the approved change. It requires no CarryChapter account, server, MCP server, or model API key.

## Install

- **Claude:** Download the Claude skill ZIP from Releases, or build it with `python3 scripts/package.py`. In Claude open **Customize → Skills**, then upload the ZIP. Enable Skills and connect Google Workspace for Docs.
- **Claude Code / Codex and other supported agents:** Use `npx skills add https://github.com/OnurCem/carrychapter` after the repository is published. For a local checkout, use `npx skills add .` from this directory.
- **ChatGPT:** Use the OpenAI plugin ZIP from Releases or generate it locally. Import or submit it where plugin upload is available. Connect Google Drive in ChatGPT and use a surface that exposes the document actions you need. A GitHub release by itself does not install the plugin into ChatGPT.

Google Docs read, write, and sharing require the corresponding connector actions and Google permissions. Availability varies by account and client. Mobile and live connector behavior have not been verified for this pilot.

## Use

1. In a new conversation, ask CarryChapter to connect your Google Doc or Markdown file. For a new topic, ask it to create a shared knowledge document.
2. After discussing something useful, ask CarryChapter to prepare a contribution. Review the changes and approve what should go into the shared source.
3. In a later conversation, connect the same source. In an existing conversation, ask “What changed?” to compare with the last version that conversation read.
4. For Docs, invite teammates through Drive or ask CarryChapter to invite a specific email with a specific role when the sharing tool is available.

Use Google sharing permissions or your repository's existing access controls. The public CarryChapter repository holds the skill itself, not your shared notes.

## Pilot check

Have two people connect the same private document from different AI clients. The first publishes a decision. The second reads it and publishes a revision. The first refreshes and sees the difference. Then make an intervening edit before approving a draft and check that the draft is revalidated before publication. Conditional writes only protect concurrent changes when the connector supports them.
