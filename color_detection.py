#!/usr/bin/python3

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

colors_data = pd.read_csv('data/first 50 colors rgb.csv')
print(colors_data)
X = colors_data.drop(columns = ['Name', 'Broad Color'])
y = colors_data['Broad Color']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)
score
print(score)
print(model.predict([[10, 200, 200]]))
