import unittest
from singly_linked_list import Node, LinkedList


def reverse_sum(x, y, carry):
    """Recurively sum the linked list by node value with carry."""
    if x is None and y is None and carry == 0:
        return None
    value = carry
    value += x.value if x else 0
    value += y.value if y else 0
    carry, value = divmod(value, 10)
    node = Node(value)
    next_x = x.next if x else None
    next_y = y.next if y else None
    node.next = reverse_sum(next_x, next_y, carry)
    return node

def forward_sum(x, y):
    x, y = _pad_zeros(x, y)
    first, carry = _forward_sum(x, y)
    return Node(carry, first) if carry else first

def _forward_sum(x, y):
    """Recursively compute (node, carry) for forward linked list node sum."""
    if x is None and y is None:
        return None, 0
    next_node, carry = _forward_sum(x.next, y.next)
    carry, val = divmod(x.value + y.value + carry, 10)
    current = Node(val, next_node)
    return current, carry
    
def _pad_zeros(x, y):
    """Pad zero nodes for the shorter linked list."""
    x_length, y_length = _len(x), _len(y)
    if x_length > y_length:
        y =  _pre_fill(y, x_length - y_length)
    else:
        x = _pre_fill(x, y_length - x_length)
    return x, y

def _pre_fill(node, n):
    """Prefill n zero nodes in front of the first node."""
    for _ in range(n):
        node = Node(0, node)
    return node

def _len(first):
    """Return linked list length given the first node."""
    counter = 0
    while first:
        counter += 1
        first = first.next
    return counter

class LinkedSumTest(unittest.TestCase):
    def setUp(self):
        self.x = LinkedList()
        self.y = LinkedList()
        self.reverse = LinkedList()
        self.forward = LinkedList()
        for i in (9, 9, 9):
            self.x.append(i)
        for i in (1,):
            self.y.append(i)
        for i in (0, 0, 0, 1):
            self.reverse.append(i)
        for i in (1, 0, 0, 0):
            self.forward.append(i)
        #for i in (7, 1, 6):
            #self.x.append(i)
        #for i in (5, 9, 2):
            #self.y.append(i)
        #for i in (2, 1, 9):
            #self.z.append(i)

    def test_reverse_sum(self):
        out = LinkedList()
        out.first = reverse_sum(self.x.first, self.y.first, 0)
        self.assertEqual(str(out), str(self.reverse))

    def test_forward_sum(self):
        out = LinkedList()
        out.first = forward_sum(self.x.first, self.y.first)
        self.assertEqual(str(out), str(self.forward))

if __name__ == '__main__':
    unittest.main()
