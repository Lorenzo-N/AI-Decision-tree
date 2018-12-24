import Dataset
import DecisionTree as DT
import DTLearn

dataset, attrs = Dataset.load_data()

s = ""
for a in attrs:
    s += a.name + ", "
print(s)

for d in dataset:
    print(d)

DT.print_tree(DTLearn.dt_learn(dataset, attrs))
