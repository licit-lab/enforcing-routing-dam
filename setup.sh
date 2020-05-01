#!/usr/bash

# Prepare miniconda instllation 
apt-get update --fix-missing && \
    apt-get install -y rsync wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
    apt-get clean

# Install conda 
 wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

# Install dependencies symuvia
add-apt-repository universe && apt-get update && apt-get install -y \
    wget bzip2 ca-certificates \
    xz-utils \
    build-essential \
    curl \
    nano \
    screen \
    rsync \
    xqilla-dev \
    libboost-all-dev \
    aptitude \
    gdal-bin \
    rapidjson-dev \
    libgdal-dev \
    unixodbc \
    libpq-dev &&\
    aptitude search -y \
    boost \
    && rm -rf /var/lib/apt/lists/* \
    && curl -SL http://releases.llvm.org/9.0.0/clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz \
    | tar -xJC . && \
    mv clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04 clang_9.0.0 && \
    echo 'export PATH=/clang_9.0.0/bin:$PATH' >> ~/.bashrc && \
    echo 'export LD_LIBRARY_PATH=/clang_9.0.0/lib:$LD_LIBRARY_PATH' >> ~/.bashrc

# Create work environment 
conda env create -f environment.yml -y