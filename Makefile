all: check coverage mutants

.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		install \
		linter \
		mutants \
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
	black --line-length 100 setup.py
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests
	flake8 --max-line-length 100 setup.py

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
	black --line-length 100 setup.py

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: install
	mutmut run --paths-to-mutate ${module} --runner 'pytest'

tests: install
	pytest --verbose