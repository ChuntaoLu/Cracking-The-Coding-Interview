class Node(object):
    """Node for singly linked list."""
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList(object):
    """Singly linked list."""
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
        return 'Linked list: [{}]'.format('->'.join(map(str, iter(self))))

    def append(self, val):
        if self.first is None:
            self.first = self.last = Node(val)
        else:
            self.last.next = Node(val)
            self.last = self.last.next
        self.length += 1

    def _remove_first(self):
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
        self.length -= 1

    def _remove_after(self, node, val):
        while node.next:
            if node.next.value == val:
                if node.next is self.last:
                    self.last = node
                node.next = node.next.next
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
