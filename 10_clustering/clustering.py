import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from pprint import pprint
# # Load data.
# data = sio.loadmat("./ex7data2.mat")["X"]
# print(data)

# Save as a file.
# np.save('./clustering', data)


# Show graph.
# x = data[:, 0]
# y = data[:, 1]
# plt.plot(x, y, "o")
# plt.show()

# The number of centroids.
K = 3
# The number of iterations.
ITERATIONS = 10


# Load data.
def load_data():
    return sio.loadmat("./ex7data2.mat")["X"]


# Initialize centroid positions.
def initialize_centroid_kmeans(X, K):
    dim = X.shape[1]
    centroids = np.random.random((K, dim))
    average = np.average(X, 0)
    centroids = centroids * average
    return centroids


def find_closest_centroids(X, centroids):
    idx = np.zeros(X.shape[0])
    for i in range(0, X.shape[0]):
        data = X[i,:]
        distance = np.linalg.norm(centroids - data, axis=1)
        argmin = np.argmin(distance)
        idx[i] = argmin
    return idx


def compute_means(X, idx, K):
    centroids = np.zeros((K, X.shape[1]))
    idx = idx + 1
    for i in range(1, K+1):
        idx_tmp = np.ones(X.shape[0]) * (idx == i)
        cnt = idx[idx==i].shape[0]
        X_tmp = X * idx_tmp[:,None]
        c = (1/cnt) * np.sum(X_tmp, axis=0)
        centroids[i-1, :] = c
    return centroids


def show_graph(X, centroids, movement):
    # Data
    x1 = X[:, 0]
    y1 = X[:, 1]
    plt.plot(x1, y1, "bo")
    plt.draw()
    # Centroid movment.
    num_of_centroids = centroids.shape[0]
    for i in range(0, num_of_centroids):
        data_x = []
        data_y = []
        for m in movement:
            pos = m[i]
            data_x.append(pos[0])
            data_y.append(pos[1])
            plt.plot(pos[0], pos[1], "rs", ms=3)
            plt.draw()
        pprint(data_x)
        pprint(data_y)
        print("--------------")
        plt.plot(data_x, data_y)
        plt.draw()

    # Centroids.
    x2 = centroids[:, 0]
    y2 = centroids[:, 1]
    plt.plot(x2, y2, "rs", ms=10)
    plt.draw()
    plt.show()




# Main
############################################
if __name__ == "__main__":

    # Load data.
    X = load_data()

    # Initialize centroid position.
    centroids = initialize_centroid_kmeans(X, K)

    # the movement of centroids.
    movement = [centroids]

    show_graph(X, centroids, movement)

    # Execute.
    for i in range(0, ITERATIONS):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        movement.append(centroids)

    show_graph(X, centroids, movement)


