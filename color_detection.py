#!/usr/bin/python3

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():
  colors_data = pd.read_csv('data/full 800 color list.csv')

  X = colors_data.drop(columns = ['Name', 'Broad Color']) # input
  y = colors_data['Broad Color']                          # output
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

  model = DecisionTreeClassifier()
  model.fit(X_train.values, y_train)
  predictions = model.predict(X_test.values)

  score = accuracy_score(y_test, predictions)
  # print(score)
  return model

# This needs to be expanded and more colors need to be added
def detect_color(model, color_array):
    # print(model.predict([[50, 168, 82]]))
  return model.predict([color_array])
