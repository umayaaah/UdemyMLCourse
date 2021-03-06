#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
t0 = time()
classifier.fit(features_train, labels_train)
print(("training time: {0}s").format(round(time()-t0, 3))) #1.407s

t1 = time()
pred = classifier.predict(features_test)
print(("prediction time: {0}s").format(round(time()-t1, 3))) #0.138s


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

print(accuracy)


#########################################################
## predicting with this particular setup takes about 30x less time than training.

