from timeit import default_timer as timer

import DTLearn
import Dataset
import DecisionTree as Dt

dataset, attrs, label = Dataset.load_data()

s = ""
for a in attrs:
    s += a.name + ", "
print(s)

for d in dataset:
    print(d)

start = timer()
tree = DTLearn.dt_learn(dataset, attrs, DTLearn.DistSettings(label, m=0))
print("Time: %.5fs" % (timer() - start))
Dt.TreePrinter().print_tree(tree)
