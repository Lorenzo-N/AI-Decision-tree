import numpy as np

import DecisionTree as Dt


class Distribution:
    label = None
    p = None
    m = None

    @staticmethod
    def settings(label=None, p=None, m=None):
        if label is not None:
            Distribution.label = label
        Distribution.p = p
        Distribution.m = m
        if (p is not None and m is not None) or (p is None and m is None):
            raise AttributeError("Set p xor m")

    def __init__(self, dataset):
        self.distribution = {}
        self.tot = len(dataset)
        for y in Distribution.label.domain:
            self.distribution[y] = sum([1 for d in dataset if d.y == y])

    def get_most_common(self):
        return max(self.distribution.items(), key=lambda item: item[1])[0]

    def get_normalized(self, y):
        return self.distribution[y] / self.tot

    def is_leaf(self):
        if Distribution.m is not None:
            return max(self.distribution.values()) >= self.tot - Distribution.m
        else:
            return max(self.distribution.values()) >= self.tot * (1 - Distribution.p)


# Cost test
# import matplotlib.pyplot as plt
# x = []
# y = []
# for i in range(11):
#     data = []
#     for j in range(i):
#         data.append(Dataset.Data([4, 3, 3, 4, 5, 4], 1))
#     for j in range(10 - i):
#         data.append(Dataset.Data([4, 3, 3, 4, 5, 4], 2))
#     dist = DTLearn.Distribution(data, DTLearn.DistSettings(label, p=0.04))
#     y.append(DTLearn.cost(dist))
#     x.append(i / 10)
# plt.plot(x, y)
# plt.show()
def cost(dist):
    s = 0
    for k in Distribution.label.domain:
        pk = dist.get_normalized(k)
        if pk != 0:
            s += pk * np.log2(pk)
    return -s


def gain(dataset, dist, attr):
    s = 0
    for v in attr.domain:
        dv = [d for d in dataset if d.x[attr.index] == v]
        if dv:
            s += len(dv) / len(dataset) * cost(Distribution(dv))
    return cost(dist) - s


def max_gain(dataset, dist, attrs):
    return attrs[np.argmax([gain(dataset, dist, a) for a in attrs])]


def dt_learn(dataset, attrs, parent_dist=None):
    if not dataset:
        return Dt.Leaf(parent_dist.get_most_common())
    dist = Distribution(dataset)
    if dist.is_leaf() or not attrs:
        return Dt.Leaf(dist.get_most_common())
    else:
        attr = max_gain(dataset, dist, attrs)
        tree = Dt.Node(attr)
        for v in attr.domain:
            dv = [d for d in dataset if d.x[attr.index] == v]
            child_attrs = [a for a in attrs if a != attr]
            subtree = dt_learn(dv, child_attrs, dist)
            tree.add_child(subtree, v)
        return tree
