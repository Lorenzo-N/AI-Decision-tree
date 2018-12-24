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


def load_data():
    file = h5py.File('plant-classification.h5', 'r')["/data/int0"]
    dataset = []
    for col, l in enumerate(file):
        for row, value in enumerate(file[col][0:10]):
            if col == 0:
                dataset.append(Data())
            if col <= 5:
                dataset[row].x.append(value)
            else:
                dataset[row].y = value
    dataset.append(Data([4, 3, 3, 4, 5, 6], 2))
    attrs = [Attr(0, "habitat", range(1, 7)), Attr(1, "colour", range(1, 5)),
             Attr(2, "leaf type", range(1, 5)), Attr(3, "leaf width", range(1, 5)),
             Attr(4, "leaf length", range(1, 5)), Attr(5, "height", range(1, 5))]
    return dataset, attrs
