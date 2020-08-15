# -*- coding: utf-8 -*-
"""K-Means Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lyLQjKNGLHzPJNshfhyGToWSuQuYx2SB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Mall_Customers.csv')

dataset.set_index('CustomerID', inplace=True)

dataset.head()

import seaborn as sns
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=dataset, hue='Genre')

X = dataset.iloc[:, [2, 3]]

from sklearn.cluster import KMeans
def elbow(X):
  wcss = []
  for i in range(1,11):
    kmean = KMeans(n_clusters=i, random_state=42) # init is kmeans++ default
    kmean.fit(X)
    wcss.append(kmean.inertia_)
  plt.plot(range(1,11),wcss)
  plt.title('The Elbow method ')
  plt.xlabel('Number of Clusters')
  plt.ylabel('WCSS')

elbow(X)

kmean = KMeans(n_clusters=5, random_state=42)
y_means = kmean.fit_predict(X)

print(y_means)

plt.scatter(X.iloc[y_means == 0,0], X.iloc[y_means == 0,1], c='red', label='Cluster 1')
plt.scatter(X.iloc[y_means == 1,0], X.iloc[y_means == 1,1], c='blue', label='Cluster 2')
plt.scatter(X.iloc[y_means == 2,0], X.iloc[y_means == 2,1], c='green', label='Cluster 3')
plt.scatter(X.iloc[y_means == 3,0], X.iloc[y_means == 3,1], c='magenta', label='Cluster 4')
plt.scatter(X.iloc[y_means == 4,0], X.iloc[y_means == 4,1], c='cyan', label='Cluster 5')
plt.scatter(kmean.cluster_centers_[:,0], kmean.cluster_centers_[:,1], s=300, c='yellow', label='Centroid')

plt.title('Cluster of incomes')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend(loc=4)

Gender =  pd.get_dummies(dataset['Genre'], drop_first=True)

dataset.drop('Genre', axis=1, inplace=True)

dataset = pd.concat([dataset, Gender], axis=1)

dataset.head()

elbow(dataset)

kmean = KMeans(n_clusters=6, random_state=42)
kmean.fit_predict(dataset)
