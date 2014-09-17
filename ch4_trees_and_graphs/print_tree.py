from itertools import zip_longest


def print_tree(root, height=None):
    """Print BST."""
    print(tree_str(root, height))

def tree_str(root, height=None):
    """Return the string representation of a BST."""
    height = height or _get_height(root)
    return _tree_str(root, height)

def _get_height(root):
    """Compute the height of a balanced BST."""
    if root is None:
        return -1
    child_height = max(_get_height(root.left), _get_height(root.right))
    return child_height + 1

def _tree_str(root, height):
    """Recursively construct the string representation of a BST."""
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
