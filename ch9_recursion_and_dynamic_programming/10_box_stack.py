import unittest


def build_box_stack(boxes, cached_stacks, bottom):
    """Recursively build the tallest stack with a given box as bottom.
    
    Returns the tallest stack based on the bottom and also caches for recursive call.
    A box stack is represented by a list which should not be mutated.
    """
    if bottom in cached_stacks:
        return cached_stacks[bottom]

    max_stack = []
    max_height = 0
    for box in boxes:
        if box in boxes[bottom][1]:
            top_stack = build_box_stack(boxes, cached_stacks, box)
            top_height = height(boxes, top_stack)
            if top_height > max_height:
                max_height = top_height
                max_stack = top_stack

    cached_stacks[bottom] = [bottom] + max_stack
    return cached_stacks[bottom]

def height(boxes, box_stack):
    """Returns the height of a box stack."""
    return sum(boxes[box][0] for box in box_stack)

def build_tallest_box_stack(boxes):
    """Returns the tallest box stack out of the given boxes."""
    cached_stacks = {}
    for box in boxes:
        build_box_stack(boxes, cached_stacks, box)
        #print('bottom: ', box, cached_stacks)
    return cached_stacks[max(cached_stacks, key=lambda x: height(boxes, cached_stacks[x]))]
    
class BoxStackTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_build_box_stack(self):
        cached_stacks = {}
        boxes = {1: (1, set()), 2: (2, {1})}
        build_box_stack(boxes, cached_stacks, 1)
        self.assertEqual({1: [1]}, cached_stacks)
        build_box_stack(boxes, cached_stacks, 2)
        self.assertEqual({1: [1], 2: [2, 1]}, cached_stacks)

    def test_build_tallest_box_stack(self):
        boxes = {1: (2, set()), 2: (1, {1, 3}), 3: (2, {1}), 4: (3, {2, 3})}
        self.assertEqual([4, 2, 3, 1], build_tallest_box_stack(boxes))

if __name__ == '__main__':
    unittest.main()
