# Backlog

- [ ] Declare `typer` and `arviz` as runtime dependencies in `pyproject.toml`; both are imported by `gatos_cli.py` and `PopulationEstimator.py`, but only the dev Dockerfile installs typer (commit `1480fb5`).
- [ ] Decide whether `compute_absence_confirmation_table` becomes a CLI command with `DOCS.md` and `CHANGELOG.md` coverage, or park it explicitly; it was added in `6dba0e4`/`bd2a8a7` with no user-facing entry point.
- [ ] Fix the 3.2.0 deprecation note in `CHANGELOG.md`, which says the command is deprecated in favor of itself (commit `0ef3a31`); name `write-cpue-and-cumulative-effort-and-captures` with `--resolution annual`.
- [ ] Remove the hardcoded developer environment from `Dockerfile.dev`, or parameterize the `mvillasante/opencode_agents` clone added in `21dbfbc`.
- [ ] Drop the stale `clean` targets for the nonexistent `gatos/calibration`, `gatos/density_functions` and `gatos/mapping` directories from `Makefile` (commit `f26772a`).
