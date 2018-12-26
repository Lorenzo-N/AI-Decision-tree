import itertools


class Node:
    def __init__(self, attr):
        self.attr = attr
        self.children = []
        self.attr_value = None

    def __str__(self):
        return "" + str(self.attr.name)

    def add_child(self, child, attr_value):
        self.children.append(child)
        child.attr_value = attr_value

    @staticmethod
    def is_leaf():
        return False


class Leaf:
    def __init__(self, y):
        self.y = y
        self.attr_value = None

    def __str__(self):
        return "y:" + str(self.y)

    @staticmethod
    def is_leaf():
        return True


# Print
class TreePrinter:
    FORK = u'\u251c'
    LAST = u'\u2514'
    VERTICAL = u'\u2502'
    HORIZONTAL = u'\u2500'
    NEWLINE = u'\u23ce'

    def __init__(self):
        self.n_leaves = 0
        self.n_nodes = 0

    def _format_newlines(self, prefix, formatted_node):
        replacement = u''.join([
            self.NEWLINE,
            u'\n',
            prefix])
        return formatted_node.replace(u'\n', replacement)

    def _format_tree(self, node, prefix=u''):
        if node.is_leaf():
            self.n_leaves += 1
            return
        self.n_nodes += 1
        children = node.children
        next_prefix = u''.join([prefix, self.VERTICAL, u'   '])
        for child in children[:-1]:
            yield u''.join([prefix,
                            self.FORK,
                            self.HORIZONTAL,
                            str(child.attr_value),
                            self.HORIZONTAL,
                            u' ',
                            self._format_newlines(next_prefix, str(child))])
            for result in self._format_tree(child, next_prefix):
                yield result

        last_prefix = u''.join([prefix, u'    '])
        yield u''.join([prefix,
                        self.LAST,
                        self.HORIZONTAL,
                        str(children[-1].attr_value),
                        self.HORIZONTAL,
                        u' ',
                        self._format_newlines(last_prefix, str(children[-1]))])
        for result in self._format_tree(children[-1], last_prefix):
            yield result

    def print_tree(self, node):
        self.n_leaves = 0
        self.n_nodes = 0
        lines = itertools.chain(
            [str(node)],
            self._format_tree(node),
            [u''],
        )
        print("\n" + u'\n'.join(lines))
        print(str(self.n_nodes) + " inner nodes, " + str(self.n_leaves) + " leaves")
