# Support Vector Machine  Classification Using Linear and RBF Kernel

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('/Users/saikalyanvytla/Desktop/python/icp-4/iris.csv')


# looking at the first 5 values of the dataset

dataset.head()


# Spliting the dataset in independent and dependent variables

X = dataset.iloc[:, :4].values  # taking only  4 features for prediction
Y = dataset['class'].values


# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)


# Fitting SVC Classification to the Training set with linear kernel

svc_linear = SVC(kernel='linear', C=1, gamma=0.1).fit(X_train, y_train)


# Accuracy of SVM Linear kernel on Training set

print('\n\nAccuracy of the SVM Linear Kernel Classification on training part is: ', svc_linear.score(X_train, y_train))


# Accuracy of SVM Linear Kernel on Test Set

print('\n\nAccuracy of the SVM Linear Kernel Classification on testing part is: ', svc_linear.score(X_test, y_test))

# Fitting SVC Classification to the Training set with rbf  kernel


svc_rbf = SVC(kernel='rbf', C=1, gamma=0.1).fit(X_train, y_train)


# Accuracy of SVM RBF kernel on Training set

print('\n\nAccuracy of the SVM RBF Kernel Classification on training part is: ', svc_rbf.score(X_train, y_train))


# Accuracy of SVM RBF Kernel on Test Set

print('\n\nAccuracy of the SVM  RBF Kernel Classification on testing part is: ', svc_rbf.score(X_test, y_test))