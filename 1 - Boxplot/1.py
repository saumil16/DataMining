# -*- coding: utf-8 -*-
"""DataMining_Lab1_ BoxPlot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZGLQqtjo-nPj3hnhfW0In7e4qpAtWnpJ
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(20)
data = np.random.normal(100, 20, 200)

plt.boxplot(data)
plt.show()

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3-q1

print("Minimum : ", data.min())
print("Quartile 1 : ", q1)
print("Mean    : ", data.mean())
print("Quartile 3 : ", q3)
print("Maximum : ", data.max())
print("Standard Deviation : ", data.std())
print("interQuartile Range : ",iqr)