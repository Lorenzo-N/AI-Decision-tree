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


class Options:
    FORK = u'\u251c'
    LAST = u'\u2514'
    VERTICAL = u'\u2502'
    HORIZONTAL = u'\u2500'
    NEWLINE = u'\u23ce'


def _format_newlines(prefix, formatted_node):
    replacement = u''.join([
        Options.NEWLINE,
        u'\n',
        prefix])
    return formatted_node.replace(u'\n', replacement)


def _format_tree(node, prefix=u''):
    if node.is_leaf():
        return
    children = node.children
    next_prefix = u''.join([prefix, Options.VERTICAL, u'   '])
    for child in children[:-1]:
        yield u''.join([prefix,
                        Options.FORK,
                        Options.HORIZONTAL,
                        str(child.attr_value),
                        Options.HORIZONTAL,
                        u' ',
                        _format_newlines(next_prefix, str(child))])
        for result in _format_tree(child, next_prefix):
            yield result

    last_prefix = u''.join([prefix, u'    '])
    yield u''.join([prefix,
                    Options.LAST,
                    Options.HORIZONTAL,
                    str(children[-1].attr_value),
                    Options.HORIZONTAL,
                    u' ',
                    _format_newlines(last_prefix, str(children[-1]))])
    for result in _format_tree(children[-1], last_prefix):
        yield result


def print_tree(node):
    lines = itertools.chain(
        [str(node)],
        _format_tree(node),
        [u''],
    )
    print(u'\n'.join(lines))
