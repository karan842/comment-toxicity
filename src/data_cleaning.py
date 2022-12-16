import os
import re
import string
import numpy as np
import pandas as pd
from itertools import groupby
import nltk
from nltk.corpus import stopwords


## DATA PREPROCESSING


# Removing duplicates, if words occured more than  2 times in comment.
def remove_duplicates(text_before):
    my_dict = dict()
    text_after = list()
    for word in text_before.split():
        if word not in my_dict.keys():
            my_dict[word] = 1
        else:
            my_dict[word] = my_dict[word] + 1
    
    for key,value in my_dict.items():
        if value>=2:
            text_after.append(key)
        else:
            text_after.append(key)
    return " ".join(text_after)


def denoise_text(text):
    """Make text lowercase, remove text in square brackets, remove links,remove punctuation
    and remove stop words containing numbers"""
    text = text.lower()                                            # Converts the text to lowercase using regex 
    text = re.sub(r"\[.*?\]","",text)                              # Replace's the text into 'nothing" if text is present inside squre brackets.
    text = re.sub("https?://\S+|www\.\S+","",text)                 # Removes the links from the comments.
    text = re.sub("<.*?>+","",text)                                # Remove unwanted
    text = re.sub("[%s]" % re.escape(string.punctuation),"",text)  # Remove punctuations
    text = re.sub("\n","",text)                                    # Remove next line symbols '\n'
    text = re.sub("\w*\d\w*","",text)                              # Takes only albhabet and digits.
    return text

## STOPWORDS
en_stop_words = stopwords.words('english')
more_stopwords = ['u', 'im', 'c', 'cu']
stop_words = en_stop_words + more_stopwords

def remove_stopwords(text):
    text = ' '.join(word for word in text.split(' ') if word not in stop_words)
    return text

# Stemming 
'''
    using snowballstemmer which is better than simple stemming 
    we are not using lemmaization because here we are looking for 
    a performance where time matters.  
    In training we are using BERT to it can understand the sentiments behinf comment_text.
'''
stemmer = nltk.SnowballStemmer("english")

def stemm_text(text):
    text = ' '.join(stemmer.stem(word) for word in text.split(' '))
    return text

'''
    As we are using BERT for predictive analysis, 
    no need to do stemming or lemmatization
    
    Bert uses BPE (Byte- Pair Encoding to shrink its vocab size), 
    so words like run and running will ultimately be decoded to run + ##ing. 
    So it's better not to convert running into run because, in some NLP problems, 
    you need that information.
'''

## Creating one parent function 

def text_data_cleaning(text):
    text = remove_duplicates(text)
    text = denoise_text(text)
    text = remove_stopwords(text)
    return text