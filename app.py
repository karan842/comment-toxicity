## Importing libraries
import numpy as np
import json
import re
import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub
from src.load_model import load_model
from prediction_service.predict import comment_toxicity_detection
from flask import Flask, request, jsonify

## Loading tf model
model_path = 'saved_models/comment-toxicity-bert.h5'
model = load_model(model_path)

## FLASK API
app = Flask(__name__)

## Definining a microservice to detect comment toxicity

@app.route('/',methods=["GET", "POST"])
def home():
    if request.method == 'GET' or request.method == 'POST':
        return "Welcome to the comment toxicity detection API. \nRoute on `detect-comment-toxicity` to detect toxicity in a comment. \n- Karan S."

        
@app.route('/detect-comment-toxicity',methods=["GET","POST"])
def predict():
    if request.method == 'POST':
        try:
            if request.json:
                comment = request.json['comment']
                print(comment)
                return jsonify((list(comment_toxicity_detection(comment, model))))
                
        except Exception as e:
            print(e)
            return {"error": e}
        
    if request.method == 'GET':
        return "Wrong method. Use POST"

if __name__ == '__main__':
    app.run(debug=False, port=4000, host='0.0.0.0')