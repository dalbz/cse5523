import sys

tfidf = [line.strip() for line in open('data\\tf-idfdata.txt')]
data = [[float(value) for value in line.rstrip(',').split(',')] for line in tfidf]

print 'data loaded'

means = [0.0 for value in data[0]]

for row in data :
    for i in range(0, len(means)) :
        means[i] += row[i]

for i in range(0, len(means)) :
    means[i] /= float(len(data))

print 'means calculated'

threshold = float(sys.argv[1])

for i in range(0, len(means)) :
    if (means[i] >= threshold) :
        for j in range(0, len(data)) :
            data[j][i] -= means[i]

print 'data adjusted'

output_file = open('data\\centered-data.txt', 'w')

for row in data:
    for value in row:
        output_file.write(str(value) + ',')
    output_file.write('\n')

output_file.close()

