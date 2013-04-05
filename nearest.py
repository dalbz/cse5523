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

artist_name = sys.argv[1]
num_neighbors = int(sys.argv[2])

artist_vec = []

for i in range(0, len(labels)):
    if (artist_name == labels[i]):
        artist_vec = data[i]

if (len(artist_vec) == 0):
    print "Artist not found"
    sys.exit()

distances = [(labels[i], sqeuclidean(numpy.array(data[i]), numpy.array(artist_vec))) for i in range(0, len(labels))]

similar = sorted(distances, key=lambda pair: pair[1])

for i in range(0, num_neighbors):
    print similar[i][0]

