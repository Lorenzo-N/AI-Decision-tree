import random

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


def char_range(c1, c2):
    return list(chr(c) for c in range(ord(c1), ord(c2) + 1))


def load_plant_data():
    # tot: 2691 (1883 / 808)
    print("Loading plant data...")
    file = h5py.File('plant.h5', 'r')["/data/int0"]
    dataset = [Data(list(x), y) for x, y in zip(zip(*file[0:6, :]), file[6])]
    random.shuffle(dataset)

    attrs = [Attr(0, "habitat", range(1, 7)), Attr(1, "colour", range(3, 5)),
             Attr(2, "leaf type", range(1, 5)), Attr(3, "leaf width", range(1, 3)),
             Attr(4, "leaf length", range(1, 5)), Attr(5, "height", range(1, 4))]
    return dataset[:1883], dataset[1883:], attrs, Label("edible", range(1, 3))


def load_krk_data():
    # tot: 28056 (19639 / 8417)
    print("Loading chess data...")
    with open('krkopt.data') as f:
        content = f.readlines()
    random.shuffle(content)
    content = [x.strip() for x in content]
    dataset = [Data(x.split(",")[:6], x.split(",")[6]) for x in content]

    for d in dataset:
        if d.y == "zero" or d.y == "one" or d.y == "two" or d.y == "three" or d.y == "four" or d.y == "five":
            d.y = "few"
        elif d.y == "six" or d.y == "seven" or d.y == "eight" or d.y == "nine" or d.y == "ten":
            d.y = "medium"
        elif d.y == "eleven" or d.y == "twelve" or d.y == "thirteen" or d.y == "fourteen" or d.y == "fifteen" \
                or d.y == "sixteen":
            d.y = "high"

    attrs = [Attr(0, "White King file", char_range('a', 'h')), Attr(1, "White King rank", char_range('1', '4')),
             Attr(2, "White Rook file", char_range('a', 'h')), Attr(3, "White Rook rank", char_range('1', '8')),
             Attr(4, "Black King file", char_range('a', 'h')), Attr(5, "Black King rank", char_range('1', '8'))]
    return dataset[:19639], dataset[19639:], attrs, Label("hand", ["draw", "few", "medium", "high"])


def load_poker_data():
    # tot: 1025010 (25010 / 1000000)
    print("Loading poker data...")
    file = h5py.File('poker.h5', 'r')
    dataset = [Data(list(map(int, x)), y) for x, y in zip(zip(*file["/data/data"]), file["/data/label"][:])]
    print("Ordering data...")
    random.shuffle(dataset)
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
