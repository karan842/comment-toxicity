<h1 align="center">COMMENT TOXICITY DETECTION⚠️💭❌</h1>

> **Caution🔞**: The text contains high amount of nasty and crude comments.


> **Warning⚠️**: I have Azure student subscription so because of limitations, I cannot keep the URL active. 

# Project Guide📖

* [About Project](#about-project)
* [Snippets](#snippets)
* [The Plan](#the-plan)
* [Approach Schema](#approach-schema)
* [Project Structure](#project-structure)
* [Run by yourself](#run-by-yourself)
* [References](#references)
* [Contact](#contact)

## [About Project](#about-project)📜
> This is an end-to-end data science project, it focuses on detecting toxicity in the comment/text. For this, I deployed a Machine Learning System into production enviornment with the help of FlaskAPI and NLP-BERT. Following MLOps lifecycle for CI/CD

## [Snippets](#snippets)📸 
### (Non-toxic vs toxic)
<img src='https://github.com/karan842/comment-toxicity/blob/master/insights/previews/nice.png' height=200px width=500px></img>  <img src='https://github.com/karan842/comment-toxicity/blob/master/insights/previews/vulgar.png' height=200px width=500px></img>

## [The Plan](#the-plan)🤔

- **Business Goal/Problem Statement:** Sometimes internet becomes the worst place, some people are spreading hate and vulgar comments on user-engaged platforms such as Instagram, Twitter, Facebook, YouTube, Amazon, etc. To stop this shameful acts we have to restrict the comment section on internet platforms for this we need some AI algorithm which can detect toxicity. The main goal of us (as ML engineers) is to create an *Machine Learning System Design*.

- **Data**: I collected this data from **Kaggle Competition** which [Toxic Comment Classification Challange](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge). The data is in the form of *text* but stored in a `.csv`. It has multiple labels for each comment in the data. Those categories are `toxic, severe_toxic, obscene, threat, insult, identity_hate`. **Caution**: The text contains high amount of nasty and crude comments.


## [Approach Schema](#approach-schema)🕊️

- Created a Project structure by creating multiple directories and files to work on it.
- Set a `Git/GitHub` for version control of code. Similarly set a `DVC` workflow for data versioning.
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

## [Project Structure](#project-structure)🧮

- **.dvc**: DVC folder for data versioning

- **.github/workflows**: GitHub Action setup
  - **master_comment-toxicity-detection.yml**: Jobs to run CI/CD pipeline for Azure
  
- **data**: It contains the .csv or .dvc data (you can download data from given website. See The [The Plan](#the-plan)
  - **processed**: Contains processed data which can be used for model building
  - **raw**: Simply a raw data un-processed.

- **insights**: Pictorial representations, visuals and graphs
  - **plots**:  Different types of plots made by `Matplotlib/Seaborn`
  - **previews**: Code snippets
  - **venn_diagram**: Venn_diagrams
  - **wordclouds**: Worclouds for text data
  
- **notebooks**: Data Analytics, model building and evaluation files `.ipynb`
  - **01_data_loading_and_EDA.ipynb**: Loading and exploring the data
  - **02_feature_enigneering_EDA2.ipynb**: Feature Engineering and EDA
  - **03_Training_BERT_model.ipynb**: Building a model
  - **04_Model_Evaluation.ipynb**: Evaluating the model performance
  
- **prediction_service**: Contains funcionalities for predicting an output by taking real time inputs
  - **predict.py**: Defined a function which can predict the output by taking text input
  
- **saved_models**: Saving the models for production
  - **comment-toxicity-bert.h5**: TF-keras model
  
- **src**: Source code to run data cleaning pipeline.
  - **data_cleaning.py**: Defined different methods to clean the text data
  - **data_split.py**: It is used for splitting the data into train/test using split ratio
  - **get_data.py**: Get the splitted data
  - **load_data.py**: Load the data into **processed** folder
  - **load_model.py**: Contains that special code of Keras which can be helpful to load Kaggle-GPU based model into local enviornment
  
- **.dockerignore**: Ignoer unnecssary folders and files for building docker image.

- **.dvcignore**: File made by [DVC](https://dvc.org/).

- **.gitattributes**: Used for pushing `.h5` model as it has 400MB size. Need [Git LFS](https://git-lfs.com/).

- **.gitignore**: To ignore unnecessary files and folders.

- **Dockerfile**: To build a Docker image.

- **app.py**: An entry file for running ML-based API using Flask.

- **dvc.lock**: File made by [DVC](https://dvc.org/).

- **dvc.yaml**: Parameters stored to run DVC workflow.

- **mlflow_experiments.py**: To run [MLFlow](https://mlflow.org/) experiments.

- **params.yaml**: Stored parameters which are useful in **src**.

- **requirements.txt**: Python dependencies to run this project.

- **template.py**: Set folders and files setup at very beginning of the project.


## [Run by yourself](#run-by-yourself)🏃🏽
1. Clone the repository: `git clone https://github.com/karan842/comment-toxicity.git`
2. Create a virtual enviornment: `python -m venv yourenv`
3. Activate virutal enviornment: `cd path/to/venv/Scripts` then `.\Activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`
5. In a **notebooks/** folder you can see `.ipynb` files which have been used for Data Analaytics, Model Building and evaluation.
6. **app.py** is an entry file to run Flask App: `python app.py`
7. Open **postman** and locate *body* tab, choose *json* and type comment in json format as shown in Snippets.

## [References](#references)📚
- [ChatGPT](https://chat.openai.com/chat)
- [Docker Image](https://hub.docker.com/r/nvidia/cuda)
- [DVC](https://dvc.org/doc/start)
- [Tensorflow Hub](https://www.tensorflow.org/hub)
- [Azure CI/CD, Container Registry](https://www.youtube.com/watch?v=BmQqBxDg2Xg)
- [O'Reilly Practical MLOps](https://www.oreilly.com/library/view/practical-mlops/9781098103002/)

## [Contact](#contact)📩
[Gmail](karanshingde@gmail.com) | [LinkedIn](https://linkedin.com/in/karanshingde) | [Twitter](https://twitter.com/KuchBhiKaran)

## Thank you for visiting🙋‍♂️
