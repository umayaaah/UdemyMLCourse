#!/usr/bin/python

"""
    This is the code to accompany the Lesson 7 regression mini-project.
    Draws a scatterplot of the training/testing data
"""    


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../tools/final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the list will be the "target" feature
### using salary to predict the bonus - r squared score: -1.485
### using long_term_incentive to predict the bonus - r squared score: -0.593
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True, sort_keys = '../tools/python2_lesson06_keys.pkl')
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"


### create and fit training set to regression
from sklearn.linear_model import LinearRegression

def fit_train():
    reg = LinearRegression()
    reg.fit(feature_train, target_train)
    acc = reg.score(feature_test, target_test)
    print("r-squared score: {0}".format(acc))
    
    return reg

def fit_test():
    reg = LinearRegression()
    reg.fit(feature_test, target_test)
    acc = reg.score(feature_train, target_train)
    print("r-squared score: {0}".format(acc))
    
    return reg

def reg_info(reg):
    print("Slope: {0}".format(reg.coef_))
    print("Intercept: {0}".format(reg.intercept_))

print("---Regression on training set with outlier---")
reg_train = fit_train()
reg_info(reg_train)

print("\n---Regression on testing set without outlier---")
reg_test = fit_test()
reg_info(reg_test)
print("\n")

### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg_train.predict(feature_test) )
    plt.plot(feature_train, reg_test.predict(feature_train), color="g")
except NameError:
    pass


plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
