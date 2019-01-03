from timeit import default_timer as timer

import DTLearn
import Dataset
import DecisionTree as Dt

training_set, test_set, attrs, label = Dataset.load_poker_data()

if len(training_set) <= 1000:
    s = ""
    for a in attrs:
        s += a.name + ", "
    print(s)
    for d in training_set:
        print(d)

print("Learning...")
DTLearn.Distribution.settings(label, p=0.00)
start = timer()
tree = DTLearn.dt_learn(training_set, attrs)
time = timer() - start

Dt.TreePrinter().print_tree(tree)
# m=0 => 143, 583, 0.01764s
# m=1 =>  85, 340, 0.01332s
# m=2 =>  70, 276, 0.01236s
# m=3 =>  37, 129, 0.01056s
print("Learning time: %.3fs" % time)
start = timer()
risk = Dataset.risk(tree, training_set)
time = timer() - start

print("Training set risk: %.2f%% in %.3fs" % (risk * 100, time))
start = timer()
risk = Dataset.risk(tree, test_set)
time = timer() - start
print("Test set risk: %.2f%% in %.3fs" % (risk * 100, time))
