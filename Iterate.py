import numpy as np
import random as r

def label_clusters(centers, data):
    """
    Labels the corresponding cluster for each point in data.
    :param centers: A numpy array representing the current predicted centers of our clusters in the shape
    (k, dimension_of_data). For example, if k=2 and we have the centers [0,0], [1,2], it would be represented as
    np.array([[0,0], [1,2]
    :param data: A numpy array representing the data we want clustered, with shape (data_size, dimension_of_data), i.e.
    Each point is an row and each dimension is a column. A collection of the points [0,1], [1,2] and [3,4] would be
    represented as np.array([[0,1], [1,2], [3,4]])
    :return: A numpy array of shape (data_size) labeling which cluster each point in data belonds to. Referencing lables
    as our returned array, cluster_of(data[i])=label[i]
    """

    centers=centers[:,None] #Append an axis of length 1 so we can broadcast data and centers to a stacked array
    #print centers.shape
    #print (data-centers).shape
    distances=np.linalg.norm(data-centers, axis=2) #Subtract every point in data with every center, broadcast the result
    #to an array of shape (k, len(Data),  dimension of data set), and find the norm of each point
    return np.argmin(distances, axis=0) #Return the min of each column, which will be the index of the closest center to
    #to the point in data at that column

def find_centers(data, cluster_indices):
    """
    Finds the mean of each cluster and
    :param data: A numpy array representing the data we want clustered, with shape (data_size, dimension_of_data), i.e.
    Each point is an row and each dimension is a column. A collection of the points [0,1], [1,2] and [3,4] would be
    represented as np.array([[0,1], [1,2], [3,4]])
    :param cluster_indices: A numpy array with k rows, each row containing the indices of all the points in data that
    belong to that cluster
    :return: A numpy array representing the centers of each cluster, in the shape (k, dimension_of_data) For example,
    if k=2 and we have the centers [0,0], [1,2], it would be represented as np.array([[0,0], [1,2]])
    """
    return np.array([np.mean(data[cluster], axis=0) for cluster in cluster_indices])

def find_cluster_indices(cluster_labels, k):
    """
    Return a numpy array of k rows, each row containing the indices in data of all the points that belong to that
    cluster
    :param cluster_labels: The cluster labels found by label_clusters(data, centers)
    :param k: The number of clusters we're grouping data into
    :return: A numpy array of k rows, each row containing the indices in data of all the points that belong to that
    cluster
    """
    clusters=np.array([None]*k)
    for i in range(k):
        clusters[i]=(np.where(cluster_labels == i))
    return clusters

def colorLabels(cluster_indices, colors, datasize, k):
    """
    Labels each point in data with the color corresponding to its cluster
    :param cluster_indices: A numpy array with k rows, each row containing the indices of all the points in data that
    belong to that cluster
    :param colors:
    :param datasize: The number of points in data
    :param k: The number of clusters we're grouping data into
    :return: A numpy array of shape (data_size) labeling the appropriate hexadecimal color for each point in data
    """
    fsakjlk=np.array(datasize)
    for i in range(k):
        fsakjlk[cluster_indices[i]]=colors[i]
    return fsakjlk

def randCenters(data,k):
    centers=np.random.rand(k, data.shape[1])
    mins=np.min(data, axis=0)
    maxes=np.max(data,axis=0)
    for dim in range(data.shape[1]):
        centers[:, dim: dim+1]*=(maxes[dim]-mins[dim])
        centers[:, dim:dim+1]+=mins[dim]
    return (centers)

def genColors(k):
    """
    Generates k random hexadecimal colors
    :param k: The number of clusters we're grouping data into
    :return: A numpy array of k hexadecimal colors
    """
    colors=np.array([None]*k)
    for i in range(k):
        colors[i]=("#%02X%02X^02X" % (r.randint(0,255), r.randint(0,255), r.randint(0,255)))
    return colors

def K_Means(data, k, max_iterations=20, tolerance=0.5):
    data_size=data.shape[0]
    centroids=randCenters(data, k)
    colors=genColors(k)
    color_data=np.array(data_size)
    for i in range(max_iterations):
        labels = label_clusters(centroids, data)
        centroids = find_centers(data, labels, 2)

X = np.repeat([[5, 5], [10, 10]], [5, 5], axis=0)
X = X + np.random.randn(*X.shape)
#centroids = np.array([[5, 5], [10, 10]])
centroids=randCenters(X, 2)
print X
for i in range(10):
    labels=label_clusters(centroids, X)
    clusters=find_cluster_indices(labels, 2)
    centroids=find_centers(X, clusters)

print centroids

#print labels, newCenters(X, labels, 2), randCenters(X, 2)
