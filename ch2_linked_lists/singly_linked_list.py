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
        node = self.first
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
        self.length -= 1
        return node

    def _remove_after(self, node, val):
        while node.next:
            if node.next.value == val:
                to_remove = node.next
                if node.next is self.last:
                    self.last = node
                node.next = to_remove.next
                self.length -= 1
                return to_remove
            node = node.next

    def remove(self, val):
        if self.first is None:
            return None
        if self.first.value == val:
            return self._remove_first()
        else:
            return self._remove_after(self.first, val)

    def _reverse(self, node):
        if node.next is None:
            return node
        prev = self._reverse(node.next)
        prev.next = node
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
            prev = current
            current = next
