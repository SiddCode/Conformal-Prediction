# TODO

## Create Agent Instructions Markdown File

Create an agent instructions file in the project root that defines guidelines for AI agents working on this codebase. The filename depends on which tool you're using.

**Filename by Tool:**
- **Qwen Code**: `qwen.md` in `.qwen/` directory (create the directory in project root)
- **OpenCode**: `AGENTS.md` in project root
- **Claude Code**: `CLAUDE.md` in project root

**Required Contents:**
- Instructions to run `ruff check` to lint the code
- Instructions to run `mypy` to check type annotations
- Note that these checks should be run before committing code
- Any project-specific conventions or patterns agents should follow
- Instructions on running the test suite (once tests are added)

**Example structure:**
```markdown
# Agent Instructions

Before making changes, run:
- `ruff check .` - Check code style and linting issues
- `mypy src/` - Check type annotations

Fix any issues found by these tools before committing changes.
```

This file will be consulted by AI agents to ensure they maintain code quality standards.
