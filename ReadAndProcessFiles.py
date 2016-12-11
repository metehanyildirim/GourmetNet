from gensim import models
from nltk.corpus import stopwords
import json
import pandas as pd
import numpy as np
import csv

cuisines = ["American (Traditional)", "American (New)", "Latin American", "Italian", "Thai",
            "Chinese", "Japanese", "Turkish", "French", "Mexican", "German", "Polish", "Greek",
            "Pakistani", "Ethiopian", "Taiwanese", "Middle Eastern", "Indian", "Korean", "Vietnamese", "Canadian", ]
list = []
lines = open("yelp_academic_dataset_business.json").readlines()
for line in lines:
    b_id = None
    cat = None
    city = None
    star = None
    rev_count = None
    cuis = "other"
    line_list = []
    jline = json.loads(line)
    for k, v in jline.items():
        if k == "review_count":
            rev_count = v
        if k == "business_id":
            b_id = v
        if k == "categories":
            cat = v
        if k == "stars":
            star = v
        if k == "city":
            city = v
    if(cat!= None):
        for cuisine in cuisines:
            if cuisine in cat:
                cuis = cuisine
                cat.remove(cuisine)
                break

    if ((cat != None) & (rev_count != None)) & (rev_count >= 10) & (("restaurants" in cat) | ("Restaurants" in cat)):
        if((b_id != None)  & (star!= None) & (city!=None)):
            line_list.append(b_id)
            line_list.append(cuis)
            line_list.append(cat)
            line_list.append(star)
            line_list.append(city)
            list.append(line_list)

my_df = pd.DataFrame(list)
my_df.to_csv('business.csv', index=False, header=False)
