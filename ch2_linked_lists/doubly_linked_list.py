class Node(object):
    """Node for doubly linked list."""
    def __init__(self, val, prev=None, next=None):
        self.value = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList(object):
    """Doubly linked list."""
    def __init__(self):
        self.first = self.last = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.first
        while node:
            yield node
            node = node.next

    def __str__(self):
        return 'Linked list: [{}]'.format('<->'.join(map(str, iter(self))))

    def append(self, val):
        if self.first is None:
            self.first = self.last = Node(val)
        else:
            node = Node(val)
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.length += 1

    def _remove_first(self):
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        self.length -= 1

    def _remove_after(self, node, val):
        while node.next:
            if node.next.value == val:
                if node.next is self.last:
                    self.last = node
                    node.next = None
                else:
                    to_remove = node.next
                    node.next = to_remove.next
                    to_remove.next.prev = node
                self.length -= 1
                return
            node = node.next

    def remove(self, val):
        if self.first is None:
            return
        if self.first.value == val:
            self._remove_first()
        else:
            self._remove_after(self.first, val)

    def _reverse(self, node):
        if node.next is None:
            node.prev = None
            return node
        prev = self._reverse(node.next)
        prev.next = node
        node.prev = prev
        node.next = None
        return node

    def reverse(self):
        if len(self) < 2:
            return
        self.first, self.last = self.last, self._reverse(self.first)

    def reverse_iterative(self):
        prev = None
        current = self.first
        self.first, self.last = self.last, self.first
        while current:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
