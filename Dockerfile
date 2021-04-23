FROM islasgeci/gatos:93b1
COPY . /workdir
WORKDIR /workdir
RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    mutmut \
    mypy \
    pandas-stubs \
    pylint \
    pylint-fail-under \
    rope
RUN pip install --upgrade pip
CMD make
