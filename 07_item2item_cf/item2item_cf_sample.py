# -*- coding: utf-8 -*-
# A sample of item-to-item Collavorate filtering.
# ref:
#   http://www.dummies.com/how-to/content/how-to-use-itembased-collaborative-filters-in-pred.html
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Input
x = np.array([
    [1,1,1,0,0,0],
    [1,1,0,0,0,0],
    [0,0,1,0,1,0],
    [0,0,1,1,1,0],
    [0,1,1,0,0,0],
    [1,1,0,1,1,0],
    [1,0,1,0,0,0],
    [0,0,0,0,0,1]
])
x = x.T

# Cosine distance.
d = pdist(x, 'cosine')
d = 1 - d
d = squareform(d)
print(d)

# 自分自身の優先度は下げる
me = np.eye(d.shape[0])
d = d - me
print(d)

# item1 - 6
for idx in range(x.shape[0]):
    print("item%d"%(idx+1))
    item1_sim = d[:,idx]
    # print(item1_sim)
    item1_rel = []
    for i in range(item1_sim.shape[0]):
        item1_rel.append(('item%d'%(i+1), item1_sim[i]))
    item1_rel = sorted(item1_rel, key=lambda d:d[1], reverse=True)
    # item1_rel = [d[0] for d in item1_rel[:3]]
    item1_rel = item1_rel[:3]
    print("   ", item1_rel)
    print("\n")














































