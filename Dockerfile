FROM python:3.13
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && \
    pip install \
    autopep8 \
    black \
    click \
    flake8 \
    hammett \
    mutmut \
    mypy \
    pandas-stubs \
    pylint \
    pylint-fail-under \
    pytest \
    pytest-cov \
    rope \
    typer

RUN pip uninstall pony --yes
RUN pip install git+https://github.com/ponyorm/pony.git
CMD make
