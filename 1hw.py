import pandas as pd
from functools import partial
import lib
import random


# tsp
df = pd.read_csv("tsp.csv")
df = df.values
x = df[:, 1]
y = df[:, 2]
size = x.shape[0]
count_dist = partial(lib.count_dist, x, y)

best_path = list(range(size))
best_dist = 1e6

for i in range(1000000):
    path = list(range(size))
    random.shuffle(path)
    dist = count_dist(path)
    if dist < best_dist:
        best_path = path
        best_dist = dist
    print(i, best_dist)

lib.build_plot(x, y, best_path)
