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
    mutmut \
    mypy \
    numpy \
    pandas \
    pandas-stubs \
    pylint \
    pylint-fail-under \
    pymc3 \
    pytest \
    rope

CMD make
