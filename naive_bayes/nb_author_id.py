#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

from time import time
import sys
sys.path.append("../tools/")

from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

##############################################################
# Enter Your Code Here
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print(f'Training time: {round(time()-t0, 3)} s')

t0 = time()
pred = clf.predict(features_test)
print(f'Predicting time: {round(time()-t0, 3)} s')

accuracy = accuracy_score(labels_test, pred)

print(f'The accuracy of Naive Bayes author identifier is {accuracy}')

##############################################################

##############################################################
'''
You Will be Required to record time for Training and Predicting 
The Code Given on Udacity Website is in Python-2
The Following Code is Python-3 version of the same code
'''

# t0 = time()
# # < your clf.fit() line of code >
# print("Training Time:", round(time()-t0, 3), "s")

# t0 = time()
# # < your clf.predict() line of code >
# print("Predicting Time:", round(time()-t0, 3), "s")

##############################################################
