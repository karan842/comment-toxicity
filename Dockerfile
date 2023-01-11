FROM pure/python:3.8-cuda10.2-cudnn7-runtime

LABEL \
    maintainer="KARAN SHINGDE <karanshingde@gmail.com>" \
    version="1.0" \
    description="Docker image with CUDA10.2 & Python 3.8" \
    python-version="3.8.x" \
    cuda-version="10.2" \
    license="Apache License 2.0"

# Set the working directory 
WORKDIR /comment-toxicity-detection-app

# Copy the current directory contents into the container at 
COPY . /comment-toxicity-detection-app

# RUN apt update \
#     && apt-mark hold cuda-command-line-tools-10-1 cuda-compat-10-1 \
#     cuda-compiler-10-1 cuda-cudart-10-1 cuda-cudart-dev-10-1 cuda-cufft-10-1 \
#     cuda-cufft-dev-10-1 cuda-cuobjdump-10-1 cuda-cupti-10-1 cuda-curand-10-1 \
#     cuda-curand-dev-10-1 cuda-cusolver-10-1 cuda-cusolver-dev-10-1 \
#     cuda-cusparse-10-1 cuda-cusparse-dev-10-1 cuda-driver-dev-10-1 \
#     cuda-gdb-10-1 cuda-gpu-library-advisor-10-1 cuda-libraries-10-1 \
#     cuda-libraries-dev-10-1 cuda-license-10-1 cuda-memcheck-10-1 \
#     cuda-minimal-build-10-1 cuda-misc-headers-10-1 cuda-npp-10-1 \
#     cuda-npp-dev-10-1 cuda-nvcc-10-1 cuda-nvdisasm-10-1 cuda-nvgraph-10-1 \
#     cuda-nvgraph-dev-10-1 cuda-nvjpeg-10-1 cuda-nvjpeg-dev-10-1 \
#     cuda-nvml-dev-10-1 cuda-nvprof-10-1 cuda-nvprune-10-1 cuda-nvrtc-10-1 \
#     cuda-nvrtc-dev-10-1 cuda-nvtx-10-1 cuda-sanitizer-api-10-1 libcudnn7 \
#     libcudnn7-dev libnccl-dev libnccl2 \
#     && apt upgrade -y \
#     && apt clean

# # Install Python 3.8 && pip
# RUN apt update \
#     && apt install -y --no-install-recommends python3 python3-pip \
#     && ln -sf python3 /usr/bin/python \
#     && ln -sf pip3 /usr/bin/pip \
#     && pip install --upgrade pip \
#     && pip install wheel setuptools

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Run app.py when the container launches
CMD ["python3", "app.py"]
