# Modern Physics Laboratory Manual

A MyST Markdown laboratory manual for PHYS 320, written to accompany the
[Modern Physics](https://github.com/QuadriviumPress/modernPhysics) textbook.
Fourteen experiments, one per week, one per chapter. This is a standalone
repository — it is not built or deployed as part of the textbook.

## Layout

```
myst.yml                    project metadata and table of contents
index.md                    schedule table and manual conventions
front-matter/                safety, notebook, uncertainty, Python, rubric
experiments/                 exp-01 … exp-14, the student handouts
instructor/                  expected values, prep notes, bill of materials
                              (excluded from the student build)
```

## Build

Use Node 22 (`nvm use` if you have nvm).

```bash
npm install
npm run start          # live preview at localhost:3000
npm run build          # static site in _build/html/
npm run verify          # metadata and structure checks
npm run check           # metadata checks plus a strict HTML build
```

Use `npm ci` when you need an exact reproducible installation from the lockfile.

To build a printable manual or a single week's handout, call `myst` directly
(installed locally via `npm install`):

```bash
npx myst build --pdf                                          # whole manual
npx myst build experiments/exp-06-plancks-constant-from-leds.md --pdf  # one week
```

The `instructor/` directory is listed under `exclude:` in `myst.yml`, so
`myst build` never renders it into the student site or PDF. Build it
deliberately:

```bash
npx myst build instructor/*.md --pdf
```

Generated output is written to `_build/` and is not committed. CI runs on
pull requests (`.github/workflows/ci.yml`); pushes to `main` deploy via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## Conventions

- Math is plain MyST: `$...$` inline, `$$...$$` display. LaTeX macros are not
  used, so any file can be printed on its own.
- Every experiment file carries a `label:` of the form `exp-<slug>`; every
  numbered question carries `q-<slug>-NN`. Cross-references use `[](#label)`.
- Values are quoted as `value ± uncertainty unit`, with the uncertainty
  rounded to one significant figure and the value rounded to match.
- Python blocks are scaffolding, not solutions: they set up the fit and leave
  the physics to the student.

## License

© 2026 Martin Veillette. Licensed under
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
Experiment content is original work, not adapted from a copyrighted source;
see [`SOURCES.md`](SOURCES.md).
