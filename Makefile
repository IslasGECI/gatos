all: check coverage mutants

.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		init \
		install \
		linter \
		mutants \
		setup \
		tests

module = gatos
codecov_token = 6b2efeba-6b2f-4225-bf99-dbe2fa826423

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests

clean:
	rm --force .mutmut-cache
	rm --recursive --force ${module}.egg-info
	rm --recursive --force ${module}/__pycache__
	rm --recursive --force ${module}/calibration/__pycache__
	rm --recursive --force ${module}/density_functions/__pycache__
	rm --recursive --force ${module}/mapping/__pycache__
	rm --recursive --force tests/__pycache__
	rm --recursive --force .pytest_cache

coverage: setup
	pytest --cov=${module} --cov-report=xml --verbose
	coverage report --show-missing

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

init: setup tests
	git config --global --add safe.directory /workdir
	git config --global user.name "Ciencia de Datos • GECI"
	git config --global user.email "ciencia.datos@islas.org.mx"

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: setup
	mutmut run --paths-to-mutate ${module} --runner 'pytest'

setup: clean install
	mkdir --parents reports/non-tabular
	mkdir --parents reports/figures

tests:
	pytest --verbose


red: format
	pytest -vm "not slow" \
	&& git restore tests/*.py \
	|| (git add tests/*.py && git commit -m "🛑🧪 Fail tests")
	chmod g+w -R .

green: format
	pytest -vm "not slow" \
	&& (git add gatos/*.py tests/*.py && git commit -m "✅ Pass tests") \
	|| git restore gatos/*.py
	chmod g+w -R .

refactor: format
	pytest -vm "not slow" \
	&& (git add gatos/*.py tests/*.py && git commit -m "♻️  Refactor") \
	|| git restore gatos/*.py tests/*.py
	chmod g+w -R .
