import numpy as np
# FUNCTION TO PREDICT THE TOXIC CLASSES ON INAPPROPRIATE COMMENTS

def comment_toxicity_detection(comment, model):
    classes = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    trained_model = model.predict([comment])
    output = np.where(trained_model > 0.5,1,0)
    for i, j in zip(classes, output[0]):
        if j==1:
            yield i, "YES" ## using 'yield' so that flask app will return all the classes with its output, if
                           ## if we use 'return' then it will break the loop and return only one class as an output
        if j==0:
            yield i, "NO"
    