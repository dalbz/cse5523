from matplotlib.mlab import PCA
import numpy as np

tfidf = [line.strip() for line in open('tf-idfdata.txt')]
data = [[float(value) for value in line.rstrip(',').split(',')] for line in tfidf]

a = np.array(data) 
U, s, V = np.linalg.svd(a, full_matrices=True)

"""
myData = numpy.array(data) 
results = PCA(myData) 

print results.Y 
"""