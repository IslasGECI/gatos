FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && \
    pip install \
    autopep8 \
    black \
    click \
    codecov \
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

CMD make
