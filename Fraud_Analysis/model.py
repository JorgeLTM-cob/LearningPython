# Author: Jorge Luis Torres Moreno
# Date: July 14th, 2021

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Since it will be needed to watch almost all the columns, the display options are modified 
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Loading data
ccd = pd.read_csv('new_credit_card.csv', index_col = 0)

# Looking how balanced is the data set
print(ccd.fraud.value_counts())
print(ccd.groupby('fraud').mean())

# Splitting the DataFrame into normal and fraudulent transactions
normal = ccd.loc[ccd.fraud == 0]
fraud = ccd.loc[ccd.fraud == 1]

# Generating statistical information about both sets
print(normal.describe())
print(fraud.describe())

# Building a sample dataset containing similar distribution of normal and fraudulent transactions
normal_sample = normal.sample(n = 70)

# Concatenating two DataFrames
new_sample = pd.concat([normal_sample, fraud], axis = 0)

# Splitting the DataFrame into Features and Targets
X = pd.DataFrame()
X['oneoff_purchases'] = new_sample.oneoff_purchases
X['purchases'] = new_sample.purchases
X['balance'] = new_sample.balance
X['credit_limit'] = new_sample.credit_limit
X['payments'] = new_sample.payments
Y = new_sample.fraud

# Splitting the data into Training data and Testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

# Model Training: Logistic Regression
model = LogisticRegression()
model.fit(X_train, Y_train)

# Model Evaluation: Accuracy Score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print("Accuracy on Training data:")
print(training_data_accuracy)

# Accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print("Accuracy on Test data:")
print(test_data_accuracy)
