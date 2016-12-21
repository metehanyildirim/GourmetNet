from gensim import models
from nltk.corpus import stopwords
import json
import numpy as np
import csv
import ast
import pandas as pd

model = models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
businesses = []
vectorized_businesses = []
vectorized_businesses2= []
with open('business.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        businesses.append([row[0],row[1], ast.literal_eval(row[2]), row[3], row[4], row[5]])


for i, business in enumerate(businesses):
    avrage_v = np.zeros((1,300))
    count = 0
    flag = False
    if len(business[2]) == 1:
        flag = True
    for cat in business[2]:
        if flag:
            count = 1
            continue
        cat = cat.lower()
        v = None
        if(cat in model):
            v = model[cat]
        elif(cat.replace(" ", "_") in model):
            v = model[cat.replace(" ", "_")]
        elif(cat.replace(" ", "") in model):
            v = model[cat.replace(" ", "")]
        if(v!=None):
            count += 1
            avrage_v = avrage_v + np.array(v)
    if(count!=0):
        avrage_v = avrage_v / count
        vectorized_businesses2.append([businesses[i][0],businesses[i][1], businesses[i][3], businesses[i][4], businesses[i][5]])
        vectorized_businesses.append([businesses[i][0],businesses[i][1], avrage_v, businesses[i][3], businesses[i][4], businesses[i][5]])
vectors = np.zeros((len(vectorized_businesses), 300))
for i,row in enumerate(vectorized_businesses):
    vectors[i] = row[2]
f = open("business_vectors.txt" ,"wb")
np.save(f, vectors)
my_df = pd.DataFrame(vectorized_businesses2)
my_df.to_csv('business_vectorized.csv', index=False, header=False)
f.close()

