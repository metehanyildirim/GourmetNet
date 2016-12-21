import json
import pandas as pd
import numpy as np
import csv
import ast

cuisines = ["American (Traditional)", "American (New)", "Latin American", "Italian", "Thai",
            "Chinese", "Japanese", "Turkish", "French", "Mexican", "German", "Polish", "Greek",
            "Pakistani", "Ethiopian", "Taiwanese", "Middle Eastern", "Indian", "Korean", "Vietnamese", "Canadian",
            "other"]
cat_index = dict(zip(cuisines , range(len(cuisines))))

review_lines = open("yelp_academic_dataset_review.json").readlines()
user_lines = open("yelp_academic_dataset_user.json").readlines()
businesses = []
users = {}
with open('business_vectorized.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        businesses.append([row[0], row[1], row[2], row[3]])
businesses = np.array(businesses)
bus_ids = businesses[:,0:1].ravel()
bus_cats = businesses[:,1:2].ravel()
bus_dict = dict(zip(bus_ids, bus_cats))
reviews = []
for review in review_lines:
    star = None
    u_id = None
    b_id = None
    line_list = []
    jreview = json.loads(review)
    for k, v in jreview.items():
        if k == "user_id":
            u_id = v
        if k == "business_id":
            b_id = v
        if k == "stars":
            star = v
    if ((b_id != None) & (u_id != None) & (star != None) & (b_id in bus_ids)):
        if (u_id in users):
            cat_stars = users[u_id][3]
            cat_stars[cat_index[bus_dict[b_id]]] += star
            revcountofcats = users[u_id][4]
            revcountofcats[cat_index[bus_dict[b_id]]] += 1
            users[u_id] = [users[u_id][0], users[u_id][1] +1 ,users[u_id][2] + star , cat_stars, revcountofcats]
        else:
            cat_stars = np.zeros((1,len(cuisines))).ravel()
            cat_stars[cat_index[bus_dict[b_id]]] = star
            revcountofcats = np.zeros((1,len(cuisines))).ravel()
            revcountofcats[cat_index[bus_dict[b_id]]] = 1
            users[u_id] = [u_id, 1, star, cat_stars, revcountofcats]

        reviews.append([u_id,b_id,star])
userlist = []
for k in users:
    users[k][2] /= users[k][1]
    users[k][3] /= users[k][4]
    userlist.append(users[k])



my_df = pd.DataFrame(userlist)
my_df.to_csv('users.csv', index=False, header=False)
my_df2 = pd.DataFrame(reviews)
my_df2.to_csv('reviews.csv', index=False, header=False)

print("reviews lenght:", len(reviews))