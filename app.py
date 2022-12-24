## Importing libraries
import pandas as pd
import numpy as np
import json
import re
import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub
from src.predict import load_model
from flask import Flask, request, jsonify

## Loading tf model
model_path = 'saved_models/comment-toxicity-bert.h5'
model = load_model(model_path)

## FLASK API
app = Flask(__name__)

## Defining the classes
classes = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# def classify(input_text, model, classes):
#     trained_model = model.predict([input_text])
#     output = np.where(trained_model > 0.5, 1, 0)
#     for i,j in zip(classes, output[0]):
#         if j==1:
#             print(f"{i} :\t YES")
#         if j==0:
#             print(f"{i} :\t NO")
            
# print(classify('Fuck you', model, classes))
        
@app.route('/detect-comment',methods=["POST"])
def index():
    if request.method == 'POST':
        try:
            if request.json:
                text = request.json['text']
                print(text)
                trained_model = model.predict([text])
                output = np.where(trained_model > 0.5, 1, 0)
                for i,j in zip(classes, output[0]):
                    if j==1:
                        print(f"{i} :\t YES")
                        return jsonify({i: "YES"})
                    if j==0:
                        print(f"{i} :\t NO")
                        return jsonify({i: "NO"})
        except Exception as e:
            print(e)
            return {"error": "Something went wrong"}

if __name__ == '__main__':
    app.run()