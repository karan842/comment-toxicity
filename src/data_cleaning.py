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


def clean_text(text):
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