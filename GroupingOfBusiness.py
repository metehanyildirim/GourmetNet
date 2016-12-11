import numpy as np
import csv
import ast
import sklearn.cluster as cluster
from gensim import models

model = models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
businesses=[]
with open('business_vectorized.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        businesses.append([row[0], row[1], row[2]])

f = open("business_vectors.txt", "rb")
vectors = np.load(f)
f.close()

kmeans = cluster.KMeans(n_clusters=100, random_state=0).fit(vectors)
a = model["hamburger"]
b = model["hotdog"]
c = model["cheeseburger"]
d = model["coke"]
e = model["fries"]

z = model["sushi"]
x = model["halal"]
y = model["steak"]
u = model["chinese"]
f = model["pencil"]
print(kmeans.predict([a,b,c,d,e,z,x,y,u,f]))
a = model["bar"]
b = model['club']
c = model["nightclub"]
d = model['shopping']
e = model["turkish"]

z = model["japanese"]
x = model["american"]
y = model["french"]
u = model["italian"]
f = model["potato"]
print(kmeans.predict([a,b,c,d,e,z,x,y,u,f]))

