import scipy
import sys
from scipy.sparse import *
from scipy.sparse.linalg import *
import numpy
import matplotlib.pyplot as plt

tfidf = [line.strip() for line in open('data\\tf-idfdata.txt')]
data = [[float(value) for value in line.rstrip(',').split(',')] for line in tfidf]

classes = [int(line.strip()) for line in open('data\\classification.txt')]
labels = [line.strip() for line in open('data\\artistList.txt')]

myData = numpy.array(data) 

print myData.shape

sparse = numpy.transpose(csc_matrix(myData))

print 'data loaded'

decomp = svds(sparse, 2)
# result = (decomp[0]*decomp[1])
result = decomp[0]

print decomp[0].shape
print decomp[1].shape
print result.shape

proj = numpy.transpose(sparse)*result

print proj.shape

reduced = proj.tolist()

x_yes = []
y_yes = []
x_no = []
y_no = []

for i in range(0, 100):
    if (classes[i] == 1):
        x_yes.append(reduced[i][0]*-1)
        y_yes.append(reduced[i][1]*-1)
    else :
        x_no.append(reduced[i][0]*-1)
        y_no.append(reduced[i][1]*-1)     

# Create 2-D Visualization of reduced data

fig = plt.figure()
sub = fig.add_subplot(1,1,1)
sub.plot(x_yes, y_yes, 'b.', x_no, y_no, 'r.')

for i in range(0, 100):
    sub.annotate(
        unicode(labels[i], "UTF-8"), 
        xy = ((reduced[i][0]*-1), (reduced[i][1]*-1)), xytext = (-20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

fig.set_size_inches(120,100)
plt.savefig('2D-Vis.png',dpi=50)

plt.show()

# Export N-D dimensional data for use in K-Means

output_file = open('data\\reduced-data.txt', 'w')

decomp = svds(sparse, int(sys.argv[1]))
# result = (decomp[0]*decomp[1])
result = decomp[0]

print decomp[0].shape
print decomp[1].shape
print result.shape

proj = numpy.transpose(sparse)*result

print proj.shape

reduced = proj.tolist()

for row in reduced:
    for value in row:
        output_file.write(str(value) + ',')
    output_file.write('\n')

output_file.close()