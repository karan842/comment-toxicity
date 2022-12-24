## This script is used to predict the class of an image using a trained deep learning model.

## Importing libraries
import numpy as np
import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub
import os

def load_model(model_path):
    """
    This function loads the model from the path specified.
    """
    load_model = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
    model = tf.keras.models.load_model(model_path, 
                                       custom_objects={'KerasLayer':hub.KerasLayer},
                                       options=load_model)
    print("Model loaded Successfully!")
    return model