import sys
import random
import scipy
from scipy.spatial.distance import sqeuclidean
from scipy.sparse import *
from scipy.sparse.linalg import *
import numpy
import matplotlib.pyplot as plt

text_data = [line.strip() for line in open('data\\reduced-data.txt')]
data = [[float(value) for value in line.rstrip(',').split(',')] for line in text_data]

labels = [line.strip() for line in open('data\\artistList.txt')]

# pre-process data

r_data = numpy.array(data) 

# get number of clusters

num_clusters = int(sys.argv[1])

# init random centers from points in dataset

centers = numpy.array([r_data[random.randint(0, r_data.shape[0])] for i in range(0, num_clusters)])

print centers.shape

# init list of cluster labales

clusters = [0 for i in range(0, r_data.shape[0]) ]

print len(clusters)

def update_clusters(clusters, centers, r_data, num_clusters):

    for i in range(0, r_data.shape[0]) :

        distances = numpy.array([sqeuclidean(r_data[i], centers[j]) for j in range(0, num_clusters)])

        clusters[i] = numpy.argmin(distances)

def update_centers(clusters, centers, r_data, num_clusters):

    new_centers = numpy.array([[0 for j in range(0, r_data.shape[1])] for i in range(0, num_clusters)])
    cluster_counts = [0 for i in range(0, num_clusters)]

    for i in range(0, r_data.shape[0]):

        current_cluster = clusters[i]

        new_centers[current_cluster] += r_data[i]

        cluster_counts[current_cluster] += 1

    for n in range(0, num_clusters):

        new_centers[n] /= float(cluster_counts[n])

    return new_centers 

n = 0
delta = 99.0

while (n < 50 and delta > 0.000001):

    update_clusters(clusters, centers, r_data, num_clusters)
    new_centers = update_centers(clusters, centers, r_data, num_clusters)

    delta = 0.0

    for i in range(0, num_clusters):
        delta += sqeuclidean(centers[i], new_centers[i])

    centers = new_centers

    n += 1

results = [[] for i in range(0, num_clusters)]

for i in range(0, r_data.shape[0]):
    results[clusters[i]].append(labels[i])

output_file = open('data\\clustering.txt', 'w')

for artist_list in results:
    output_file.write(str(artist_list))
    output_file.write('\n\n')

output_file.close()