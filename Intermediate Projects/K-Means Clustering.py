import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.random.rand(100, 2)
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_)
plt.show()
