# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

### Changed

### Removed

## [3.0.0] - 2026-06-19
### Changed
- Changed pymc3 to pymc latest version.
- Upgrade `geci-plots==0.9*` dependency.
- `run_loo_diagnostic` now saves LOO results as scalars instead of arrays, and no longer passes `ax` to `plot_khat`.
- `run_model_diagnostics` no longer calls `run_waic_diagnostic`.

### Removed
- Unused `eradication-data-requirements` dependency.
- Removed `run_waic_diagnostic` method and its associated test helper `assert_dict_equal_from_path`. WAIC diagnostics is no longer supported by pymc latest version.

## [2.1.0] - 2025-12-15
### Added
- Add cli command `plot-annual-captures-effort` to generate an annual summart of captures and effort plot.
- Add DeprecationWarning to `get_capture_and_effort_by_zone()`

## [2.0.2] - 2025-06-17

### Fixed
- Method `probability` from class `CalculatorPValue` now calculates high value from data.

## [2.0.1] - 2023-09-28

### Added
- Add cli object to executable path. This way we can use it without `typer-cli`

## [2.0.0] - 2023-09-15

### Removed
- Export all code related with reggae plot

## [1.1.0] - 2023-08-28

### Added
- Add `write_progress_probability_figure`

### Removed
- Remove test `tests_populationEstimator::test_run` to improve suit test speed


## [1.0.0] - 2023-07-25

### Fixed
- Fix typo in interface command `write_yearly_cumulative_effort_and_captures`

### Changed

### Removed

[unreleased]: https://github.com/IslasGECI/gatos/compare/v2.0.0...HEAD
[2.1.0]: https://github.com/IslasGECI/gatos/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/IslasGECI/gatos/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/IslasGECI/gatos/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/IslasGECI/gatos/compare/v0.2.2...v1.0.0
