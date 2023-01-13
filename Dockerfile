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


# Install any needed packages specified in requirements.txt
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Run app.py when the container launches
CMD ["python3", "app.py"]
