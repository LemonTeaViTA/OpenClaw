---
name: self-improvement
description: "Injects self-improvement reminder during agent bootstrap"
metadata:
  {
    "openclaw":
      {
        "emoji": "🧠",
        "events": ["agent:bootstrap"],
        "install": [{ "id": "self-improving-agent", "kind": "skill", "label": "Self-Improving Agent" }],
      },
  }
---

# Self-Improvement Hook

Injects a reminder to evaluate learnings during agent bootstrap.

## What It Does

- Fires on `agent:bootstrap` (before workspace files are injected)
- Adds a reminder block to check `.learnings/` for relevant entries
- Prompts the agent to log corrections, errors, and discoveries

## Configuration

No configuration needed. Enable with:

```bash
openclaw hooks enable self-improvement
```
