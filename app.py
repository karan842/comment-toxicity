'''
Author: Karan Shingde

'''

## Importing libraries
import pandas as pd
import numpy as np
import json
import re
import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub
from flask import Flask

## Loading tf model

model_path = 'saved_models\comment-toxicity-bert.h5'

load_model = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')

model = tf.keras.models.load_model(model_path, 
                                   custom_objects={hub:'KerasLayer'},
                                   options=load_model)
print("Model loaded Successfully!")

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

if __name__ == '__main__':
    app.run()