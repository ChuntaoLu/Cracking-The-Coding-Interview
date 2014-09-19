from itertools import zip_longest


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

    def show_tree(self):
        return tree_str(self)

class NodeWithParent(Node):
    """Node with link to its parent."""
    def __init__(self, data=None, left=None, right=None, parent=None):
        super().__init__(data, left, right)
        if left:
            left.parent = self
        if right:
            right.parent = self
        self.parent = parent

def print_tree(root, height=None):
    """Print tree."""
    print(tree_str(root, height))

def tree_str(root, height=None):
    """Return the string representation of a tree."""
    height = height or _get_height(root)
    return _tree_str(root, height)

def _get_height(root):
    """Compute the height of a tree."""
    if root is None:
        return -1
    child_height = max(_get_height(root.left), _get_height(root.right))
    return child_height + 1

def _tree_str(root, height):
    """Recursively construct the string representation of a tree."""
    spaces = ' ' * (2 ** (height + 1) - 1)
    if root is None:
        return (spaces * 2 + '  \n') * (height + 1)
    top = spaces + str(root.data).center(2) + spaces + '\n'
    left = _tree_str(root.left, height - 1)  
    right = _tree_str(root.right, height - 1)
    bottom = ''
    for l, r in zip_longest(left.split('\n'), right.split('\n'), fillvalue=''):
        r = r or ' ' * len(l)
        bottom += l + r + '\n'
    return top + bottom
