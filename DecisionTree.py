class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def get(self):
        return self.key

    def add_child(self, child):
        self.children.append(child)


class DecisionTree:
    def __init__(self):
        self.root = None
