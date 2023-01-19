<h1 align="center">COMMENT TOXICITY DETECTION⚠️💭❌</h1>

# About Project📜
This is an end-to-end data science project, it focuses on detecting toxicity in the comment/text using Deep Learning based API.

## The Plan🤔

- **Business Goal/Problem Statement:** Sometimes internet becomes the worst place, some people are spreading hate and vulgar comments on user-engaged platforms suxh as Instagram, Twitter, Facebook, YouTube, Amazon, etc. To stop this shameful acts we have to restrict the comment section on internet platforms for this we need some AI algorithm which can detect toxicity. The main goal of us (as ML engineers) is to create an *Machine Learning System Design*.

- **Data**: I collected this data from **Kaggle Competition** which [Toxic Comment Classification Challange](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge). The data is in the form of *text* but stored in a `.csv`. It has multiple labels for each comment in the data. Those categories are `toxic, severe_toxic, obscene, threat, insult, identity_hate`. **Caution**: The text contains high amount of nasty and crude comments.

## Approach🕊️
- Created a Project structure by creating multiple directories and files to work on it.
- Set a `Git/GitHub` for version control of code. Similarly set a `DVC` workflow for versioning the data.
- In a *notebooks* folder you can find some notebooks where I explored the data using Python.
- Cleaned the text data by applying various text analytics techniques such HTML parser, removing stopwords, etc.
- In very first step I started performing feature engineering and EDA on the train data to gain a pattern of textual comments, frequent n-words, etc. 
- Set a DVC pipeline for data cleaning which contains data loading, text cleaning and data saving in *data* folder.
- To build an AI algorithm I trained the cleaned data on Kaggle GPU. For training I've used `BERT` pre-trained model with some required modification for input and outputs.
- Trained the model using `Tensorflow and Keras` deep learning library and saved the model locally in `.h5` format you can find the model in *saved_models* directory.
- Next step is deployment, where I choosed `Flask` web framework to deploy this Machine Learning system into a microservice API.
- To load the model I added some special Keras code which gives stability to the GPU environment.
- Served an algorithm in a URL of API `/detect-comment-toxicity` using `Flask`. Tested the APIs using `Postman`.
- I used `Docker Engine` for containerization of the GPU based Flask App.
- I created a *.dockerfile* which can run GPU based Flask App in the container.
- Built up the `Azure Container Registry` and pushed the Docker image to it. Simultaneously created an `Azure app service` for Docker Container.
- Set up the CI/CD workflow for continous integration and continous deployment.
