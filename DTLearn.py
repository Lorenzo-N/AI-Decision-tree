import DecisionTree as Dt


class DistSettings:
    def __init__(self, label, p=None, m=None):
        self.label = label
        self.p = p
        self.m = m


class Distribution:
    def __init__(self, dataset, dist_settings):
        self.distribution = {}
        self.tot = len(dataset)
        self.dist_settings = dist_settings
        for y in dist_settings.label.domain:
            self.distribution[y] = sum([1 for d in dataset if d.y == y])

    def get_most_common(self):
        return max(self.distribution.items(), key=lambda item: item[1])[0]

    def get_normalized(self):
        return [d / self.tot for d in self.distribution.values()]

    def is_leaf(self):
        return max(self.distribution.values()) >= self.tot - self.dist_settings.m


def dt_learn(dataset, attrs, dist_settings, parent_dataset=None):
    if not dataset:
        dist = Distribution(parent_dataset, dist_settings)
        return Dt.Leaf(dist.get_most_common())
    dist = Distribution(dataset, dist_settings)
    if dist.is_leaf() or not attrs:
        return Dt.Leaf(dist.get_most_common())
    else:
        attr = attrs[0]
        tree = Dt.Node(attr)
        for v in attr.domain:
            dv = [d for d in dataset if d.x[attr.index] == v]
            child_attrs = [a for a in attrs if a != attr]
            subtree = dt_learn(dv, child_attrs, dist_settings, dataset)
            tree.add_child(subtree, v)
        return tree
