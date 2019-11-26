FROM islasgeci/base:19c0
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
RUN conda install --yes --channel bokeh bokeh && \
    conda install --yes --channel conda-forge phantomjs selenium && \
    conda install --yes --channel https://conda.binstar.org/pymc pymc
RUN apt-get update && apt-get install --yes \
    git \
    texlive-full
