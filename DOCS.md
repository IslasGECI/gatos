# Public interface

## `gatos`

### gatos write-cpue-and-cumulative-effort-and-captures --input-path --resolution --output-path
Writes a CSV table of catch-per-unit-effort and cumulative effort and captures for each period.
Parameters: `--input-path` is a CSV of capture records; `--resolution` is `annual` (default), `semestral` or `monthly`; `--output-path` is the destination CSV.
Returns: a CSV with columns `Date`, `Effort`, `Cumulative_captures`, `CPUE`.
Notes: `Date` values have the form `YYYY-P1` (annual), `YYYY-P1`–`YYYY-P2` (semestral), or `YYYY-P1`–`YYYY-P12` (monthly). Effort and captures accumulate in period order; `CPUE` is per period.

### gatos plot-annual-effort-and-captures --input-path --output-path --show-mean-line
Writes a yearly chart of cumulative effort and cats dispatched.
Parameters: `--input-path` is a CSV of capture records; `--output-path` is the destination PNG; `--show-mean-line` adds a mean-effort line (default off).
Returns: a PNG chart at `--output-path`.

### gatos write-monthly-effort-and-captures-by-zone --input-path --output-path
Writes a monthly summary of effort and captures for each working zone.
Parameters: `--input-path` is a CSV of capture records with zone information; `--output-path` is the destination CSV.
Returns: a CSV with columns `Date` (year and month), `Zone`, `Effort`, `Captures`.

### gatos write-effort-and-captures-by-zone-for-year --input-path --output-path --year
Writes a yearly summary of effort and captures for each working zone in one selected year.
Parameters: `--input-path` is a CSV of capture records with zone information; `--output-path` is the destination CSV; `--year` is the year to keep (default `2022`).
Returns: a CSV with columns `Date` (year), `Zone`, `Effort`, `Captures`.

### gatos version
Prints the installed package version.
Returns: the version string on standard output.

### gatos write-yearly-cumulative-effort-and-captures --input-path --output-path
Writes a CSV table of yearly cumulative effort and captures.
Parameters: `--input-path` is a CSV of capture records; `--output-path` is the destination CSV.
Returns: a CSV with columns `Date`, `Effort`, `Cumulative_captures`, `CPUE`.
Notes: Deprecated since 3.2.0; scheduled for removal in 4.0.0. Use `gatos write-cpue-and-cumulative-effort-and-captures --resolution annual` instead.

## `crea_tabla_pvalor`

### crea_tabla_pvalor calculate --resource --posterior --output-file
Writes a JSON summary of captured cats, remaining cats and eradication probabilities.
Parameters: `--resource`/`-r` is a CSV of captures; `--posterior`/`-p` is a CSV of population estimates; `--output-file`/`-o` is the destination JSON.
Returns: a JSON file with keys `gatos_capturados`, `probabilidades`, `gatos_remanentes`.

## `crea_tamagno_poblacion_gatos`

### crea_tamagno_poblacion_gatos calculate --resource --output-file --iterations --datapackage
Estimates the initial population size and writes the estimate distribution and diagnostics.
Parameters: `--resource`/`-r` is the input data resource; `--output-file`/`-o` is the destination CSV for the estimate distribution; `--iterations`/`-i` sets the simulation length (default `1000000`); `--datapackage`/`-d` selects data-package input (default `true`, set to `false` for a plain CSV).
Returns: a CSV estimate distribution and diagnostic files in `reports/non-tabular/` and `reports/figures/`.
