import unittest
from doubly_linked_list import LinkedList, Node


class AnimalQueueSingle(object):
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, animal):
        self.queue.append(animal)

    def dequeue_any(self):
        return self.queue._remove_first()

    def dequeue_dog(self):
        return self.queue.remove('dog')

    def dequeue_cat(self):
        return self.queue.remove('cat')

class AnimalQueueDouble(object):
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.order = 0

    def enqueue(self, animal):
        if animal == 'dog':
            self.dogs.append((animal, self.order))
        else:
            self.cats.append((animal, self.order))
        self.order += 1

    def dequeue_any(self):
        if self.dogs.first is None:
            return self.dequeue_cat()
        if self.cats.first is None:
            return self.dequeue_dog()
        cat = self.cats.first
        dog = self.dogs.first
        if cat.value[1] < dog.value[1]:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()

    def dequeue_dog(self):
        return self.dogs._remove_first()

    def dequeue_cat(self):
        return self.cats._remove_first()
   
class AnminalQueueSingleTest(unittest.TestCase):
    def setUp(self):
        self.aq = AnimalQueueSingle()
        self.aq.enqueue('cat')
        self.aq.enqueue('dog')
        self.aq.enqueue('dog')
        self.aq.enqueue('cat')
        self.cat1 = self.aq.queue.first
        self.dog1 = self.aq.queue.first.next

    def test_dequeue_any(self):
        self.assertEqual(self.aq.dequeue_any(), self.cat1)

    def test_dequeue_dog(self):
        self.assertEqual(self.aq.dequeue_dog(), self.dog1)

    def test_dequeue_cat(self):
        self.assertEqual(self.aq.dequeue_cat(), self.cat1)

class AnminalQueueDoubleTest(AnminalQueueSingleTest):
    def setUp(self):
        self.aq = AnimalQueueDouble()
        self.aq.enqueue('cat')
        self.aq.enqueue('dog')
        self.aq.enqueue('dog')
        self.aq.enqueue('cat')
        self.cat1 = self.aq.cats.first
        self.dog1 = self.aq.dogs.first

if __name__ == '__main__':
    unittest.main()
