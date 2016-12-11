import numpy as np
import csv
import ast
import pandas as pd

businesses = []
with open('business.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        businesses.append([row[0], ast.literal_eval(row[1]), row[2], row[3]])

freqs = {}
for i, business in enumerate(businesses):
    for cat in business[1]:
        cat = cat.lower()
        if cat in freqs:
            freqs[cat] = freqs[cat] + 1
        else:
            freqs[cat] = 1

for a in freqs:
    print(a, freqs[a])