import sys
import random

# get the portion of the data to use as training
# the rest will be used as test
training_ratio = float(sys.argv[1])

tfidf = [line.strip() for line in open('data/tf-idfdata.txt')]

data = [[float(value) for value in line.rstrip(',').split(',')] for line in tfidf]

classes = [int(line.strip()) for line in open('data/classification.txt')]

artists = [line.strip() for line in open('data/artistList.txt')]

training_file = open('data/svmlight/svmlight_train.txt', 'w')
test_file = open('data/svmlight/svmlight_test.txt', 'w')

for i in range(0, len(data)):

    output = test_file

    if (random.random() <= training_ratio):
        # put item in training set
        output = training_file

    output.write(str(classes[i]) + ' ')

    for j in range(0, len(data[i])):
        if (data[i][j] > 0.00001):
            output.write(str(j + 1) + ':' + str(data[i][j]) + ' ')

    output.write('# ' + str(artists[i]) + '\n')

    print artists[i]

training_file.close()
test_file.close()