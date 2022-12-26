# syntax=docker/dockerfile:1
FROM python-3.9-alpine
EXPOSE 0806
WORKDIR /comment-toxicity-detection-app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]