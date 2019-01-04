import sys
from timeit import default_timer as timer

import DTLearn
import DecisionTree


def find_y(node, x):
    if node.is_leaf():
        return node.y
    return find_y(next(child for child in node.children if child.attr_value == x[node.attr.index]), x)


def risk(tree, test_set):
    return sum([1 for d in test_set if find_y(tree, d.x) != d.y]) / len(test_set)


def print_p_table(data):
    training_set, test_set, attrs, label = data
    print("\n")
    print("  p   |  learn  | training | test set")
    print("      |  time   | set risk | risk")
    print("-------------------------------------")
    for p in range(0, 101, 5):
        out = "\r%4.1f%% |   ..." % (p / 10)
        sys.stdout.write(out)
        DTLearn.Distribution.settings(label, p=p / 1000)
        start = timer()
        tree = DTLearn.dt_learn(training_set, attrs)
        out = out[:-6] + " %6.3fs |   ..." % (timer() - start)
        sys.stdout.write(out)
        out = out[:-6] + "  %.3f%%  |  ..." % (risk(tree, training_set) * 100)
        sys.stdout.write(out)
        out = out[:-5] + " %.3f%%\n" % (risk(tree, test_set) * 100)
        sys.stdout.write(out)


def print_m_table(data):
    training_set, test_set, attrs, label = data
    print("\n")
    print("  m   |  learn  | training | test set")
    print("      |  time   | set risk | risk")
    print("-------------------------------------")
    for m in range(0, 21):
        out = "\r  %2d  |   ..." % m
        sys.stdout.write(out)
        DTLearn.Distribution.settings(label, m=m)
        start = timer()
        tree = DTLearn.dt_learn(training_set, attrs)
        out = out[:-6] + " %6.3fs |   ..." % (timer() - start)
        sys.stdout.write(out)
        out = out[:-6] + "  %.3f%%  |  ..." % (risk(tree, training_set) * 100)
        sys.stdout.write(out)
        out = out[:-5] + " %.3f%%\n" % (risk(tree, test_set) * 100)
        sys.stdout.write(out)


def print_tree(data, p=None, m=None):
    training_set, test_set, attrs, label = data
    print("Learning...")
    DTLearn.Distribution.settings(label, p, m)
    start = timer()
    tree = DTLearn.dt_learn(training_set, attrs)
    time = timer() - start

    DecisionTree.TreePrinter().print_tree(tree)
    print("Learning time: %.3fs" % time)
    start = timer()
    r = risk(tree, training_set)
    time = timer() - start

    print("Training set risk: %.2f%% in %.3fs" % (r * 100, time))
    start = timer()
    r = risk(tree, test_set)
    time = timer() - start
    print("Test set risk: %.2f%% in %.3fs" % (r * 100, time))