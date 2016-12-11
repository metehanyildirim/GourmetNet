import numpy as np


f = open("business_vectors.txt", "rb")
print(np.load(f).shape)
f.close()