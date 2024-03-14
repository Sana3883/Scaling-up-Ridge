ROM continuumio/miniconda3
WORKDIR /app

RUN conda install -c conda-forge git pip numpy scipy cython joblib threadpoolctl pytest compilers
RUN apt update -y && apt install -y gcc g++
RUN pip install  git+https://github.com/Sana3883/scikit-learn.git


RUN conda install -c conda-forge dask-jobqueue
RUN conda install -c conda-forge asyncssh
RUN conda install -c conda-forge dask-mpi

RUN apt install -y vim

RUN conda install -c conda-forge "libblas=*=*mkl"
RUN conda install -c conda-forge bokeh
Run pip install jupyter-server-proxy

ENV MKL_NUM_THREADS=32

