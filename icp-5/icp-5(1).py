from sklearn.cluster import KMeans
from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('/Users/saikalyanvytla/Desktop/python/icp-5/College - College.csv')
x = dataset.iloc[:,[3,4,7,8]]
y = dataset.iloc[:-1]
# see how many samples we have of each species
print(dataset["University"].value_counts())
sns.FacetGrid(dataset, hue="University", size=4).map(plt.scatter, "Accept", "Enroll")
# do same for petals
sns.FacetGrid(dataset, hue="University", size=4).map(plt.scatter, "F.Undergrad", "P.Undergrad")
plt.show()
# note that the species are nearly linearly separable with petal size,but sepal sizes are more mixed.


scaler = preprocessing.StandardScaler()

scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


nclusters = 3 # this is the k in kmeans
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)

from sklearn import metrics
wcss = []
##elbow method to know the number of clusters
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()