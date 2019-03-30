import numpy as np

def iterate(centers, data):
    centers=centers[:,None] #Append an axis of length 1 so we can broadcast data and centers to a stacked array
    distances=np.linalg.norm(data-centers, axis=2) #Subtract every point in data with every center, broadcast the result
    #to an array of shape (k, len(Data),  dimension of data set), and find the norm of each point
    #Tolerance = np.minimum of each row sum
    return np.argmin(distances, axis=0) #Return the min of each column, which will be the index of the closest center to
    #to the point in data at that column

def newCenters(data, labels, k):
    indices=[]
    for i in range(k):
        indices.append(np.where(labels==i))
    return np.array([np.mean(data[cluster], axis=0) for cluster in indices])

def randCenters(data,k):
    centers=np.random.rand(k, data.shape[1])
    mins=np.min(data, axis=0)
    maxes=np.max(data,axis=0)
    for dim in range(data.shape[1]):
        centers[:, dim: dim+1]*=(maxes[dim]-mins[dim])
        centers[:, dim:dim+1]+=mins[dim]
    return (centers)

X = np.repeat([[5, 5], [10, 10]], [5, 5], axis=0)
#X = X + np.random.randn(*X.shape)
#centroids = np.array([[5, 5], [10, 10]])
centroids=randCenters(X, 2)
print centroids

for i in range(1000):
    labels=iterate(centroids, X)
    centroids=newCenters(X, labels, 2)

print centroids

#print labels, newCenters(X, labels, 2), randCenters(X, 2)
