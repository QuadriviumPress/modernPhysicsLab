# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run start
npm run build
npm run verify
npm run check
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `verify` runs `node scripts/verify-book.mjs`.
- Experiments live under `experiments/`, not `chapters/ch-NN-slug.md`. Instructor notes stay in `instructor/` and are excluded from the student build.
- No media plugins. The handouts do not embed simulations, animations, video, or H5P activities.

## Presentation gap

Experiments use `{exercise}` directives and do not attach a hidden `{solution}` dropdown. Solution markup is deferred.
