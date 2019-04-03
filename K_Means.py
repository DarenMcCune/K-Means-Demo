import numpy as np
import random as r

def k_means(data, k, max_iterations=20, tolerance=0):
    centers=random_centers(data, k)
    colors=random_colors(k)
    for i in range(max_iterations):
        prev_centers=centers
        centers, clusters, color_labels=k_means1(data, k, centers, colors)

        for cluster in clusters:
            #If we encounter an empty cluster we're going to need to start over
            if(len(cluster)==0):
                print("here")
                return k_means(data, k, max_iterations, tolerance)

        if(np.mean(np.linalg.norm(prev_centers-centers,axis=0))<=tolerance):
            break

    return centers, clusters, colors, color_labels

def k_means1(data, k, centers=[], colors=None):
    """if(centers==[]):
        centers=random_centers(data, k)
        colors=random_colors(k)"""

    labels=label_clusters(data, centers)
    clusters=find_cluster_indices(labels, k)
    centers=find_centers(data, clusters)
    color_labels=None
    color_labels=label_colors(data.shape[0], clusters, colors, k)

    return centers, clusters, color_labels


def label_clusters(data, centers):
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

    centers = centers[:,None] # Append an axis of length 1 so we can broadcast data and centers to a stacked array
    distances  = np.linalg.norm(data-centers, axis=2)  # Subtract every point in data with every center, broadcast the
    # result to an array of shape (k, len(Data),  dimension of data set), and find the norm of each point
    return np.argmin(distances, axis=0)  # Return the min of each column, which will be the index of the closest center
    # to the point in data at that column


def find_centers(data, cluster_indices):
    """
    Finds the mean of each cluster and
    :param data: A numpy array representing the data we want clustered, with shape (data_size, dimension_of_data), i.e.
    Each point is an row and each dimension is a column. A collection of the points [0,1], [1,2] and [3,4] would be
    represented as np.array([[0,1], [1,2], [3,4]])
    :param cluster_indices: A numpy array with k rows, each row containing the indices of all the points in data that
    belong to that cluster
    :return: A numpy array representing the centers of each cluster, in the shape (k, dimension_of_data). For example,
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


def label_colors(data_size, cluster_indices, colors, k):
    """
    Labels each point in data with the color corresponding to its cluster
    :param cluster_indices: A numpy array with k rows, each row containing the indices of all the points in data that
    belong to that cluster
    :param colors:
    :param data_size: The number of points in data
    :param k: The number of clusters we're grouping data into
    :return: A numpy array of shape (data_size) labeling the appropriate hexadecimal color for each point in data
    """

    color_labels=np.array([None]*data_size)
    for i in range(k):
        color_labels[cluster_indices[i]]=colors[i]
    return color_labels

def random_centers(data, k):
    """
    Randomly generates k centers in the range of data
    :param data: A numpy array representing the data we want clustered, with shape (data_size, dimension_of_data), i.e.
    Each point is an row and each dimension is a column. A collection of the points [0,1], [1,2] and [3,4] would be
    represented as np.array([[0,1], [1,2], [3,4]])
    :param k: The number of clusters we're grouping data into
    :return: A numpy array representing the ramdomly selected centers of k clusters, in the shape (k, dimension_of_data).
    For example, if k=2 and we have the centers [0,0], [1,2], it would be represented as np.array([[0,0], [1,2]])
    """
    centers=np.random.rand(k, data.shape[1])
    mins=np.min(data, axis=0)
    maxes=np.max(data,axis=0)
    for dim in range(data.shape[1]):
        centers[:, dim: dim+1]*=(maxes[dim]-mins[dim])
        centers[:, dim:dim+1]+=mins[dim]
    return (centers)

def random_colors(k):
    """
    Generates k random hexadecimal colors
    :param k: The number of clusters we're grouping data into
    :return: A numpy array of k hexadecimal colors
    """
    colors=np.array([None]*k)
    for i in range(k):
        colors[i]=("#%02X%02X%02X" % (r.randint(0,255), r.randint(0,255), r.randint(0,255)))
    return colors

