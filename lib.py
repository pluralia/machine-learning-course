import copy
import random
import matplotlib.pyplot as plt


def points_dist(x1, y1, x2, y2):
    dist = 0
    if x1 != x2:
        dist += abs(x2 - x1)
    if y1 != y2:
        dist += abs(y2 - y1)
    return dist


def count_dist(x, y, idxs):
    dist = 0
    for i in range(1, len(idxs)):
        fr, to = idxs[i - 1], idxs[i]
        dist += points_dist(x[fr], y[fr], x[to], y[to])
    return dist


def plot_l1(x1, y1, x2, y2):
    if x1 != x2:
        plt.arrow(x1, y1, x2 - x1, 0, color='r', shape='full', length_includes_head=True, head_width=15.)
        x1 = x2
    if y1 != y2:
        plt.arrow(x1, y1, 0, y2 - y1, color='r', shape='full', length_includes_head=True, head_width=15.)


def build_plot(x, y, idxs):
    plt.figure()
    dist = 0
    for i in range(1, len(idxs)):
        fr, to = idxs[i - 1], idxs[i]
        plot_l1(x[fr], y[fr], x[to], y[to])
    plt.scatter(x, y, c='black')
    plt.title(f'Distance length: {count_dist(x, y, idxs)}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
