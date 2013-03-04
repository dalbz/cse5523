from svmlight import DocumentFactory, Learner

artists = [line.strip() for line in open('artistList.txt')]
tags = [line.strip() for line in open('tagData.txt')]
classes = [line.strip() for line in open('classification.txt')]

f = DocumentFactory()
docs = [f.new(x.split(',')) for x in tags]
l = Learner()
l.set_kernel_type(0)
model = l.learn(docs[50:], [int(s) for s in classes[50:]])
judgments = [model.classify(d) for d in docs[:50]]
print model.plane, model.bias
print judgments

i = 0;
while (i < len(judgments)):

    print str(i) + '. ' + artists[i]

    if (judgments[i] >= 0.0):
        print 'yes'
    else :
        print 'no'

    i += 1
