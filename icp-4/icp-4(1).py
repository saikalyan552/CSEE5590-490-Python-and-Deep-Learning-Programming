# Naive Bayes Classification

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd

# sklearn.naive_bayes.GaussianNB(priors=None, var_smoothing=1e-09)

# Importing the dataset

dataset = pd.read_csv('/Users/saikalyanvytla/Desktop/python/icp-4/iris.csv')


# looking at the first 5 values of the dataset

dataset.head()


# Spliting the dataset in independent and dependent variables

X = dataset.iloc[:, :4].values
Y = dataset['class'].values


# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)


# Fitting Naive Bayes Classification to the Training set with linear kernel

nvclassifier = GaussianNB()
nvclassifier.fit(X_train, y_train)

# Predicting the Test set results

y_pred = nvclassifier.predict(X_test)

# lets see the actual and predicted value side by side

y_compare = np.vstack((y_test, y_pred)).T

# actual value on the left side and predicted value on the right hand side
# printing the top 5 values

print(y_compare[:5, :])


# Accuracy of NavesBayes on Training Sets
print('Accuracy of Naive Bayes classifier on training set: {:.2f}'
     .format(nvclassifier.score(X_train, y_train)))

# Accuracy of NavesBayes on Testing Sets
print('Accuracy of Naive Bayes classifier on test set: {:.2f}'
     .format(nvclassifier.score(X_test, y_test)))


# print the accuracy score of predicted and actual values on test set

print('\n\nAccuracy of the Naive Bayes Classification on Test Data Prediction is : ', metrics.accuracy_score(y_test, y_pred))

# Plot the Test Prediction , Test Value on Graph

plt.scatter(y_test, y_pred)

plt.xlabel('True Values')

plt.ylabel('Predictions')

plt.show()