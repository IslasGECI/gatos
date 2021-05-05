all: mutants

module = gatos
codecov_token = 92c09c8a-f80e-4220-af6d-1b8bb79be8f1

.PHONY: all check clean coverage format install linter mutants tests

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

coverage: install
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants:
	mutmut run --paths-to-mutate ${module}

tests: install
	pytest --verbose