import h5py


class Data:
    def __init__(self, x=None, y=None):
        if x is None:
            x = []
        self.x = x
        self.y = y

    def __str__(self):
        return "x:" + str(self.x) + "  y:" + str(self.y)


class Attr:
    def __init__(self, index, name, domain):
        self.index = index
        self.name = name
        self.domain = domain


class Label:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain


def load_plant_data():
    # tot: 2691 (2153 / 538)
    print("Loading plant data...")
    file = h5py.File('plant.h5', 'r')["/data/int0"]
    dataset = [Data(list(x), y) for x, y in zip(zip(*file[0:6, :]), file[6])]
    attrs = [Attr(0, "habitat", range(1, 7)), Attr(1, "colour", range(1, 5)),
             Attr(2, "leaf type", range(1, 5)), Attr(3, "leaf width", range(1, 5)),
             Attr(4, "leaf length", range(1, 6)), Attr(5, "height", range(1, 7))]
    return dataset[:2153], dataset[2153:], attrs, Label("edible", range(1, 3))


def load_poker_data():
    # tot: 1025010 (25010 / 1000000)
    print("Loading poker data...")
    file = h5py.File('poker.h5', 'r')
    dataset = [Data(list(map(int, x)), y) for x, y in zip(zip(*file["/data/data"]), file["/data/label"][:])]
    print("Ordering data...")
    # ordering data
    for d in dataset:
        cards = [(d.x[0], d.x[1]), (d.x[2], d.x[3]), (d.x[4], d.x[5]),
                 (d.x[6], d.x[7]), (d.x[8], d.x[9])]
        cards.sort(key=lambda c: c[1])
        d.x = [x for c in cards for x in c]

    attrs = [Attr(0, "Suit 1", range(1, 5)), Attr(1, "Rank 1", range(1, 14)),
             Attr(2, "Suit 2", range(1, 5)), Attr(3, "Rank 2", range(1, 14)),
             Attr(4, "Suit 3", range(1, 5)), Attr(5, "Rank 3", range(1, 14)),
             Attr(6, "Suit 4", range(1, 5)), Attr(7, "Rank 4", range(1, 14)),
             Attr(8, "Suit 5", range(1, 5)), Attr(9, "Rank 5", range(1, 14))]
    return dataset[:25010], dataset[25010:], attrs, Label("hand", range(0, 10))


def load_seq_data(n):
    file = h5py.File('artificial-sequence.h5', 'r')
    for i in file["/data/signal"]:
        print(i)
    dataset = [Data(list(map(int, x)), y) for x, y in zip(zip(*file["/data/data"][:, 0:n]),
                                                          file["/data/label"][0:n])]
    attrs = [Attr(0, "S1", range(1, 5)), Attr(1, "C1", range(1, 14)),
             Attr(2, "S2", range(1, 5)), Attr(3, "C2", range(1, 14)),
             Attr(4, "S3", range(1, 5)), Attr(5, "C3", range(1, 14)),
             Attr(6, "S4", range(1, 5)), Attr(7, "C4", range(1, 14)),
             Attr(8, "S5", range(1, 5)), Attr(9, "C5", range(1, 14))]
    return dataset, attrs, Label("hand", range(0, 10))


def find_y(node, x):
    if node.is_leaf():
        return node.y
    return find_y(next(child for child in node.children if child.attr_value == x[node.attr.index]), x)


def risk(tree, test_set):
    return sum([1 for d in test_set if find_y(tree, d.x) != d.y]) / len(test_set)
