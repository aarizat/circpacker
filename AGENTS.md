# AGENTS.md — circpacker modernization guide

## Mission
Modernize this repository to current (2026) Python best practices while keeping behavior correct.

## Current modernization status
Completed:
- uv + pyproject.toml workflow is in place
- pytest suite exists and runs in CI
- ruff formatting/linting is enforced
- baseline dependency cleanup has started

Next required milestone:
- Add type hints to core modules and public API.
- Introduce a type-check gate (`ty check`) in CI (initially pragmatic config; exclude non-core paths if needed).

Non-goals:
- Rewriting algorithms unless necessary for correctness or compatibility.
- Introducing heavy frameworks.

## Canonical runtime + tooling
- Python: 3.13 (target), support 3.12+ only if feasible without complexity.
- Package manager + env: `uv`
- Test runner: `pytest`
- Lint/format: `ruff` (use `ruff format` and `ruff check`)
- Type checking: `ty` (run as `uv run ty check`)

## Source layout and packaging
Preferred layout:
- `src/circpacker/...` (src-layout)
- `tests/...`
- `pyproject.toml` (PEP 621 metadata)
- `uv.lock` checked in

If the repo currently uses `setup.py`, `requirements.txt`, or ad-hoc scripts:
1) migrate metadata and dependencies into `pyproject.toml`
2) keep a minimal compatibility shim ONLY if needed, but prefer removing legacy packaging files.

## “Dignified Python” rules (mandatory)
Before changing Python code, load the local skill:
- `.opencode/skills/dignified-python-313/SKILL.md`

Key rules to enforce across the refactor:
- Use Python 3.13+ type syntax: `list[str]`, `dict[str, int]`, `X | None`
- Prefer LBYL over EAFP for expected conditions (don’t use exceptions for control flow)
- Use `pathlib.Path` instead of `os.path`
- Use `abc.ABC` + `@abstractmethod` for interfaces (when an interface is needed)
- Absolute imports by default; avoid relative imports

## Workflow the agent must follow (do not skip)

### 1) Baseline discovery
- Identify: entrypoints, public API, CLI (if any), expected inputs/outputs.
- Try to run something minimal (import, help, demo script).
- Create/expand tests that pin down current behavior before large refactors.

### 2) Create modern project scaffold
- Create `pyproject.toml` with:
  - project metadata (name, version, description)
  - dependencies
  - optional `project.scripts` if CLI exists
  - ruff + pytest + ty config
- Create `uv.lock`:
  - `uv sync`
- Add `README.md` updates showing how to:
  - install: `uv sync`
  - run: `uv run ...`
  - test: `uv run pytest`

### 3) Testing strategy
- Start with “characterization tests”:
  - if functions exist: test deterministic outputs
  - if CLI exists: use `pytest` + `subprocess.run(..., check=True)` and assert stdout/stderr/exit-code
- Avoid brittle tests. Prefer pure-function tests.
- Add regression tests for any bug you fix.

### 4) Deprecation & dependency cleanup
- Audit imports for deprecated libs / modules.
- Replace deprecated APIs (stdlib + third-party).
- Prefer well-maintained libs; remove unused deps.
- If a dependency is unmaintained:
  - replace it, or
  - isolate it behind a small adapter layer to ease later replacement.

### 5) Architecture improvements (lightweight, pragmatic)
- Split monolithic modules into:
  - `core/` (pure algorithms)
  - `io/` (file parsing/serialization)
  - `cli/` (only if there is a CLI)
- Keep functions small:
  - reduce nesting via early returns
  - introduce helper functions rather than huge parameter lists
- Introduce “ports/adapters” only where it genuinely helps testability.

### 6) CI (must add / must keep green)
CI must run:
- `uv sync`
- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run ty check`
- `uv run pytest`

### 7) Definition of Done (DoD)
A modernization PR is done when:
- `uv sync` works on a clean machine
- `uv run pytest` passes
- ruff passes (format + lint)
- `uv run ty check` passes for the core modules (initial config may exclude non-core paths if needed)
- Core public functions/classes have type hints using modern syntax (`list[str]`, `X | None`)
- README contains correct commands
- no dead code / obvious deprecations remain

## Refactor policy
- Work in small PR-sized steps.
- Add/adjust tests before risky refactors.
- No behavior changes without tests.

## How to validate instructions are being read
At the start of a work session, the agent MUST:
1) Quote (verbatim) the “Next required milestone” bullets and the “Canonical runtime + tooling” bullets,
2) List the exact commands it plans to run first (3-8 commands),
3) State explicitly: “Loaded dignified-python-313 rules” before writing/refactoring Python.
