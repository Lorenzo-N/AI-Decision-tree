import DecisionTree
import h5py

tree = DecisionTree.Node(1)
tree.add_child(DecisionTree.Node(3))
tree.add_child(DecisionTree.Node(4))
tree.add_child(DecisionTree.Node(5))
tree.children[1].add_child(DecisionTree.Node(5))

DecisionTree.print_tree(tree)

f = h5py.File('plant-classification.h5', 'r')
dset = f["/data/int0"]

D = []
for col, l in enumerate(dset):
    for row, value in enumerate(dset[col][0:10]):
        if len(D) <= row:
            D.append({"x": [], "y": []})
        if col <= 5:
            D[row]["x"].append(value)
        else:
            D[row]["y"].append(value)

for row in D:
    print(row)
