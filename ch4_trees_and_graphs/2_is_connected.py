import unittest
from collections import deque


def is_connected_dfs(digraph, start, target):
    """Check if directed graph which is represented by a dict has
    a route from 'start' to 'target' using DFS.
    
    Make sure not do duplicate checks!
    """
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        #print('checking ', node)
        for vertex in digraph[node]:
            if vertex not in visited:
                if vertex == target:
                    return True
                visited.add(vertex)
                stack.append(vertex)
    return False

def is_connected_bfs(digraph, start, target):
    """Check if directed graph which is represented by a dict has
    a route from 'start' to 'target' using BFS.
    
    Make sure not do duplicate checks!
    """
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        #print('checking ', node)
        for vertex in digraph[node]:
            if vertex not in visited:
                if vertex == target:
                    return True
                visited.add(vertex)
                queue.append(vertex)
    return False
    

class IsConnectedTest(unittest.TestCase):
    def setUp(self):
        self.digraph = {1: [2], 2: [4], 3: [2, 4], 4: [1], 5: [2, 3]} 

    def test_is_connected_dfs_true(self):
        self.assertTrue(is_connected_dfs(self.digraph, 5, 1))
        self.assertTrue(is_connected_dfs(self.digraph, 3, 1))
        self.assertTrue(is_connected_dfs(self.digraph, 1, 2))
    
    def test_is_connected_dfs_false(self):
        self.assertFalse(is_connected_dfs(self.digraph, 1, 5))
        self.assertFalse(is_connected_dfs(self.digraph, 2, 3))
        self.assertFalse(is_connected_dfs(self.digraph, 4, 5))
    
    def test_is_connected_bfs_true(self):
        self.assertTrue(is_connected_bfs(self.digraph, 5, 1))
        self.assertTrue(is_connected_bfs(self.digraph, 3, 1))
        self.assertTrue(is_connected_bfs(self.digraph, 1, 2))
    
    def test_is_connected_bfs_false(self):
        self.assertFalse(is_connected_bfs(self.digraph, 1, 5))
        self.assertFalse(is_connected_bfs(self.digraph, 2, 3))
        self.assertFalse(is_connected_bfs(self.digraph, 4, 5))

if __name__ == '__main__':
    unittest.main()
