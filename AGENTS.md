# AGENTS.md

## Public interface
The supported interface is the end-user command line: the executable programs declared in `[tool.flit.scripts]` of `pyproject.toml`, with their subcommands and options. Python modules, helpers and classes are internal, even when importable from `gatos` or covered by tests. `DOCS.md` lists the elements; `CHANGELOG.md` records only changes to them.

## Verification
- `make check` runs `black --check --line-length 100` on `gatos/` and `tests/`, then `flake8` with `.flake8` (max line 100, complexity 18, E203/E266/E501/W605 ignored). It needs only the dev tools installed by `Dockerfile`.
- `make coverage` depends on `setup`: `clean` → `pip install --editable .` → create `reports/non-tabular/` and `reports/figures/` → `pytest --cov=gatos --cov-report=xml --verbose` → `coverage report --show-missing`.
- Focused loop: `pytest -m "not slow"`; the `slow` marker is declared in `pytest.ini` and marks tests that call installed console scripts via `subprocess`.
- Runtime imports (`pandas`, `pymc`, `geci_plots`, `metadata_wrangler`) come from the package requirements; `Dockerfile` installs only dev tools, so a bare environment can pass `make check` and still fail test collection with `ModuleNotFoundError` until `make install` runs.
- Tests use paths relative to the repository root and write outputs under `tests/data/`, `reports/`, and `posterior.csv` in the working directory; run them from `/workdir`.
- `make init_git` sets the global `safe.directory` for `/workdir` and the GECI author identity; without that entry git may reject commands with "dubious ownership".
- `make all` chains `check`, `coverage`, `mutants`; `mutants` runs `mutmut run --paths-to-mutate gatos --runner 'pytest' || mutmut html`, and CI uploads the resulting `html/` directory.

## Entrypoints and flow
- `[tool.flit.scripts]` maps three console programs to one Typer app and two Click groups with a `calculate` subcommand; Click programs use short flags (`-r`, `-p`, `-o`, `-i`, `-d`).
- `gatos/__init__.py` wildcard-imports four modules and defines `__version__`; the CLI `version` command echoes that value.

## Conventions and preserved constraints
- Commit stream alternates 🛑🧪 Fail tests, ✅ Pass tests and ♻️ Refactor commits; the `red`, `green` and `refactor` Makefile recipes implement that flow with `black`, `pytest -m "not slow"`, `git add`, `git commit` and `git restore`.
- Input CSV columns are `Fecha`, `Esfuerzo`, `Capturas` (and `Zona`); CLI output tables use `Date`, `Effort`, `Captures`, `CPUE`; aggregated periods are `YYYY-Pn` (`P1` annual, `P1`–`P2` semestral, `P1`–`P12` monthly).
- Model diagnostics write to `reports/non-tabular/` and `reports/figures/`, so those directories must exist before running estimation commands.
