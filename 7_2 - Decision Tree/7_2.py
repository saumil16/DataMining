# -*- coding: utf-8 -*-
"""DataMining_Lab7_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mH1q89F9Sgal9eQHHpAWIKHEUBk0APGF
"""

import pandas as pd

df = pd.read_csv('/content/diabetes_dataset.csv')
df.head()

x = df.drop('Outcome',axis=1)
y = df.Outcome

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

model = DecisionTreeClassifier()

model = model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)

confusion_matrix(y_test,y_pred)

print("Accuracy:",(78+32)/(78+21+23+32))

print(classification_report(y_test,y_pred))

model.predict([[6,148,72,35,0,33.6,0.627,50]])

from sklearn.tree import export_graphviz
from io import StringIO
from IPython.display import Image
import pydotplus

feature = x.columns
feature

#Model based on GINI
dot_data = StringIO()
export_graphviz(model, out_file=dot_data,filled=True,special_characters=True,feature_names = feature,class_names=['0','1'],max_depth=6)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes_set.png')
Image(graph.create_png())

#Model based on Entropy

model = DecisionTreeClassifier(criterion="entropy", max_depth=3)

model = model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)

dot_data = StringIO()
export_graphviz(model, out_file=dot_data,filled=True, rounded=True,special_characters=True, feature_names = feature,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes_set.png')
Image(graph.create_png())