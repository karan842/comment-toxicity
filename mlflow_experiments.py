import mlflow
import mlflow.tensorflow
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import hamming_loss

from sklearn.model_selection import train_test_split

from src.load_model import load_model
from src.data_cleaning import text_data_cleaning

# defiing list of classes
list_classes = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# loading data
train = pd.read_csv('data/raw/train.csv')
test = pd.read_csv('data/raw/test.csv')

# Applying data cleaning
train['comment_text_clean'] = train['comment_text'].apply(lambda x: text_data_cleaning(x))
test['comment_text_clean'] = test['comment_text'].apply(lambda x: text_data_cleaning(x))

# target and train data
target_data = train[list_classes]
train_data = train['comment_text_clean']

# Splitting data into train and test
X_train, X_test, y_train, y_test = train_test_split(train_data, target_data, test_size=0.2, random_state=42)

## Loading tf model
model_path = 'saved_models/comment-toxicity-bert.h5'
model = load_model(model_path)

# Evaluate the model
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)

# Metrics for Multi-label classification
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
f1_score = f1_score(y_test, y_pred, average='weighted')
hm_loss = hamming_loss(y_test, y_pred)

print("Running MLFlow")
# Start MLflow run
def mlflow_run():
    with mlflow.start_run():
        
        # Set MLFlow experiment
        mlflow.set_experiment("detect-comment-toxicity-bert")
    
        # Log metrics
        mlflow.log_metric({
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "hamming_loss": hm_loss,
        })
        
        # Log model
        mlflow.log_model(model, "model")
        
        # log the metrics in json format in artifacts
        result = {
            "accuracy": accuracy.tolist(),
            "precision": precision.tolist(),
            "recall": recall.tolist(),
            "f1_score": f1_score.tolist(),
            "hamming_loss": hm_loss.tolist()
        } 
        
        mlflow.log_artifact(json.dumps(result), "metrics.json")
    
if __name__ == "__main__":
    mlflow_run()
    print("MLflow run completed successfully")
