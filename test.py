from svmlight import DocumentFactory, Learner

f = DocumentFactory()
docs = [f.new(x.split()) for x in [
        "this is a nice long document",
        "this is another nice long document",
        "this is rather a short document",
        "a horrible document",
        "another horrible document"]]
l = Learner()
l.set_kernel_type(1)
model = l.learn(docs, [1, 1, 1, -1, -1])
judgments = [model.classify(d) for d in docs]
print model.plane, model.bias
print judgments