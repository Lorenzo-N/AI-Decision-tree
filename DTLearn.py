import DecisionTree as DT


def check_all(dataset):
    y = dataset[0].y
    for d in dataset:
        if d.y != y:
            return None
    return y


def dt_learn(dataset, attrs):
    if len(dataset) == 0:
        return DT.Leaf(0)
    y = check_all(dataset)
    if y is not None:
        return DT.Leaf(y)
    elif len(attrs) == 0:
        return DT.Leaf(-1)
    else:
        attr = attrs[0]
        tree = DT.Node(attr)
        for v in attr.domain:
            dv = [d for d in dataset if d.x[attr.index] == v]
            child_attrs = [a for a in attrs if a != attr]
            subtree = dt_learn(dv, child_attrs)
            tree.add_child(subtree, v)
        return tree
