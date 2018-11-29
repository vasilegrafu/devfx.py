import numpy as np 
import pandas as pd 
import sklearn as sk
import sklearn.cluster
import devfx.data_vizualization.seaborn as dv

while True:

    # These are ceters of the clusters
    center1 = np.array([1, 1])
    center2 = np.array([5, 8])
    center3 = np.array([9, 1])
    center4 = np.array([5, -5])

    # We generate data around centers of the clusters
    data1 = np.random.randn(256, 2) + center1
    data2 = np.random.randn(256, 2) + center2
    data3 = np.random.randn(256, 2) + center3
    data4 = np.random.randn(256, 2) + center4
    data = np.concatenate((data1, data2, data3, data4), axis=0)

    # k-means algorithm
    kmeans = sk.cluster.KMeans(n_clusters=4)
    kmeans.fit(data)

    figure = dv.Figure(size=(8, 8))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(data[:,0], data[:,1], c=kmeans.labels_, cmap='rainbow')
    chart.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='*', color='red')
    figure.show()






