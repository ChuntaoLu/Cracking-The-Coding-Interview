import unittest
from singly_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()

    def test_len(self):
        self.assertEqual(len(self.l), 0)

    def test_append_to_empty_list(self):
        self.l.append(0)
        self.assertEqual(self.l.first.value, 0)
        self.assertEqual(self.l.last.value, 0)
        self.assertEqual(len(self.l), 1)

    def test_append_to_none_empty_list(self):
        self.l.append(0)
        self.l.append(1)
        self.assertEqual(self.l.first.value, 0)
        self.assertEqual(self.l.first.next.value, 1)
        self.assertEqual(len(self.l), 2)

    def test_str_of_empty_list(self):
        self.assertEqual(str(self.l), "Linked list: []")

    def test_str_of_one_node_list(self):
        self.l.append(0)
        self.assertEqual(str(self.l), "Linked list: [0]")

    def test_str_of_multiple_nodes_list(self):
        self.l.append(0)
        self.l.append(1)
        self.assertEqual(str(self.l), "Linked list: [0->1]")
    
    def test_remove_from_empty_list(self):
        old = self.l
        self.l.remove(0)
        self.assertEqual(self.l, old)

    def test_remove_from_one_node_list(self):
        old = self.l
        self.l.append(0)
        self.l.remove(0)
        self.assertEqual(self.l, old)

    def test_remove_from_two_nodes_list(self):
        self.l.append(0)
        old = self.l
        self.l.append(1)
        self.l.remove(1)
        self.assertEqual(self.l, old)

    def test_remove_first_from_multiple_nodes_list(self):
        for v in range(3):
            self.l.append(v)
        self.l.remove(0)
        self.assertEqual(str(self.l), "Linked list: [1->2]")

    def test_remove_middle_from_multiple_nodes_list(self):
        for v in range(3):
            self.l.append(v)
        self.l.remove(1)
        self.assertEqual(str(self.l), "Linked list: [0->2]")

    def test_remove_last_from_multiple_nodes_list(self):
        for v in range(2):
            self.l.append(v)
        old = self.l
        self.l.append(2)
        self.l.remove(2)
        self.assertEqual(self.l, old)

    def test_remove_none_existing_node(self):
        for v in range(3):
            self.l.append(v)
        old = self.l
        self.l.remove(4)
        self.assertEqual(self.l, old)

if __name__ == '__main__':
    unittest.main()
