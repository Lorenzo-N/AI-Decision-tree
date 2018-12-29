from timeit import default_timer as timer

import DTLearn
import Dataset
import DecisionTree as Dt

dataset, attrs, label = Dataset.load_data()

s = ""
for a in attrs:
    s += a.name + ", "
print(s)

# for d in dataset:
#     print(d)
DTLearn.Distribution.settings(label, m=2)
start = timer()
tree = DTLearn.dt_learn(dataset, attrs)
time = timer() - start

Dt.TreePrinter().print_tree(tree)
# m=0 => 143, 583, 0.01764s
# m=1 =>  85, 340, 0.01332s
# m=2 =>  70, 276, 0.01236s
# m=3 =>  37, 129, 0.01056s
print("Time: %.5fs" % time)
print("Risk: %.2f%%" % (DTLearn.risk(tree, dataset) * 100))
