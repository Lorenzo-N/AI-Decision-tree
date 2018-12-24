import itertools


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return "" + str(self.value);

    def get(self):
        return self.value

    def add_child(self, child):
        self.children.append(child)


class Options(object):
    FORK = u'\u251c'
    LAST = u'\u2514'
    VERTICAL = u'\u2502'
    HORIZONTAL = u'\u2500'
    NEWLINE = u'\u23ce'


def _format_newlines(prefix, formatted_node, options):
    replacement = u''.join([
        options.NEWLINE,
        u'\n',
        prefix])
    return formatted_node.replace(u'\n', replacement)


def _format_tree(node, options, prefix=u''):
    children = list(node.children)
    next_prefix = u''.join([prefix, options.VERTICAL, u'   '])
    for child in children[:-1]:
        yield u''.join([prefix,
                        options.FORK,
                        options.HORIZONTAL,
                        options.HORIZONTAL,
                        u' ',
                        _format_newlines(next_prefix,
                                         str(child),
                                         options)])
        for result in _format_tree(child,
                                   options,
                                   next_prefix):
            yield result
    if children:
        last_prefix = u''.join([prefix, u'    '])
        yield u''.join([prefix,
                        options.LAST,
                        options.HORIZONTAL,
                        options.HORIZONTAL,
                        u' ',
                        _format_newlines(last_prefix,
                                         str(children[-1]),
                                         options)])
        for result in _format_tree(children[-1],
                                   options,
                                   last_prefix):
            yield result


def print_tree(node):
    lines = itertools.chain(
        [str(node)],
        _format_tree(node, Options()),
        [u''],
    )
    print(u'\n'.join(lines))
