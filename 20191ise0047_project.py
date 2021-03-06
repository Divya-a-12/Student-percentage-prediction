# -*- coding: utf-8 -*-
"""20191ISE0047_PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tDpQnXD0goA05sA-24daS1ZN6y4oFXl-

***In this regression task we will predict the percentage of marks that a student is expected to score based upon the number of hours they studied.***
"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Reading the data to a dataframe

data=pd.read_csv("/content/scorehours.csv")
print(data)
print(data.shape)
print(data.describe())

# Since the dataset is quiet small so visualizing the data will give a better picture of the correlation between variables.
data.plot(x="Hours",y="Scores",style='o')
plt.title("Hours vs Percentage")
plt.xlabel("Hours Studied")
plt.ylabel("Scores Obtained")
plt.show()

#From the scatter plot it can be observed that there is a positive correlation between the No. of hours studied and the scores obtained by the student
data.plot(kind='box')
plt.show()

#Preparing data for model
#Feature and target variables
X = data.Hours
y = data.Scores

#Splitting data into train and test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
X_train = np.array(X_train).reshape(-1,1)
X_test = np.array(X_test).reshape(-1,1)
y_train = np.array(y_train).reshape(-1,1)
y_test = np.array(y_test).reshape(-1,1)

#Model training
#Model training

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

#Accuracy
lr.score(X_test, y_test)

#Model Evaluation
#Plotting results

plt.scatter(data.Hours, data.Scores, marker = '+', color = 'blue')
plt.plot(data.Hours, lr.predict(data[['Hours']]), color = 'red')  #plotting the line of best fit
plt.xlabel('No. of Hours')
plt.ylabel('Scores')

#Model evluation

from sklearn import metrics

predictions = lr.predict(X_test)
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

#Making predictions
#Making predictions using trained model

inp = float(input("Enter hours studied: "))
y_pred = lr.predict([[inp]])
s = str(y_pred)
print("Predicted Score: {}" .format(s[2:-2]))