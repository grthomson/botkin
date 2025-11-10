# Botkin — LLM from scratch

This repo follows a learn-then-harden approach:
- `study/` mirrors the book’s flow (chapter-by-chapter experiments).
- `src/botkin/` holds reusable code promoted from `study/`.
- `ops/` will contain Docker/CI/CD for serving later.

## Layout
- `study/` — notebooks & summary scripts per chapter.
- `src/botkin/` — package code (tokenizers, models, training, utils).
- `configs/` — experiment configs.
- `data/` — datasets (gitignored).
- `experiments/` — logs/checkpoints (gitignored).
- `ops/` — deployment/CI (placeholders for now).
