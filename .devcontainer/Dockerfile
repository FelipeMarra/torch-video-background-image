FROM nvcr.io/nvidia/pytorch:24.06-py3

RUN apt-get -yqq update && \
    apt-get install -yq --no-install-recommends ca-certificates expat libgomp1 && \
    apt-get autoremove -y && \
    apt-get clean -y

RUN apt-get install -y bash \
    autoconf \
    automake \
    build-essential \
    cmake \
    git-core \
    libass-dev \
    libfreetype6-dev \
    libgnutls28-dev \
    libmp3lame-dev \
    libnuma1 \
    libnuma-dev \
    libsdl2-dev \
    libtool \
    libva-dev \
    libvdpau-dev \
    libvorbis-dev \
    libxcb1-dev \
    libxcb-shm0-dev \
    libxcb-xfixes0-dev \
    libc6 \
    libc6-dev \
    meson \
    ninja-build \
    pkg-config \
    texinfo \
    unzip \
    wget \
    yasm \
    zlib1g-dev && \
    apt-get -yqq update

# Miniconda
COPY .devcontainer/env.yml .

RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm -rf ~/miniconda3/miniconda.sh && \
    ~/miniconda3/bin/conda init bash && \
    ~/miniconda3/bin/conda init zsh && \
    ~/miniconda3/bin/conda env update --file env.yml

# FFMPEG
RUN git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git && \
    cd nv-codec-headers && \
    make install

RUN git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg/ && \
    cd ffmpeg && \
    ./configure \
    --prefix="$CONDA_PREFIX"\
    --enable-nonfree \
    --enable-cuda-nvcc \
    --enable-libnpp \
    --extra-cflags=-I/usr/local/cuda/include \
    --extra-ldflags=-L/usr/local/cuda/lib64 \
    --disable-static \
    --enable-shared && \
    make -k -j 8 && \
    make install && \
    ldconfig

ENV LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH