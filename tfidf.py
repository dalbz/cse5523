from collections import Counter
from collections import defaultdict
import math

artists = [line.strip() for line in open('data/artistList.txt')]
tagLists = [line.strip() for line in open('data/tagStrings.txt')]
countLists = [line.strip() for line in open('data/tagCounts.txt')]

tags = [line.rstrip(',').split(',') for line in tagLists]

countStrings = [line.rstrip(',').split(',') for line in countLists]
counts = []

for row in countStrings:
    counts.append([(int(value) + 1) for value in row]);

docs_with_term = Counter()

tagMapList = []

for i in range(0, len(artists)):

    # increment the number of documents with each tag

    for tag in tags[i]:
        docs_with_term[tag] += 1

    # create a map of terms to term counts for each artist

    tagCountMap = defaultdict(int)

    for j in range(0, len(counts[i])):
        tagCountMap[tags[i][j]] = counts[i][j]

    tagMapList.append(tagCountMap)

# create a list of terms 

termlist = []

for term in docs_with_term.keys():
    termlist.append(term)

print docs_with_term

# output the new tf-idf representation

output_file = open('data/tf-idfdata.txt', 'w')

for i in range(0, len(artists)):
    for term in termlist:

        # don't really need to normalize since the last.fm
        # data already was
        tf = tagMapList[i][term]

        idf = math.log(len(artists) / float(1 + docs_with_term[term]))

        tfidf = tf*idf 

        output_file.write(str(tfidf) + ',')

    output_file.write('\n')

    print artists[i]


output_file.close()