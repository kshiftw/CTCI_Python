""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
import unittest
from unittest import TestCase


def route_between_nodes(graph: dict, first_node: int, second_node: int) -> bool:
    """ Given a graph represented by an adjacency list, determine whether two nodes have a route between them.

    Assumption:
    - All node values in the graph are unique and are positive integers.

    Idea:
    - DFS search through the adjacency list until the second_node is found. If not found, there are no routes between.

    Complexity:
    - Time: O(N) - need to access all nodes if route doesn't exist or the node is the last node we look at
    - Space: O(N) - visited array needs to store up to N values

    Approach:
    - Recursively call has_route with each adjacent vertex (neighbour)
    - Mark visited vertices so that we avoid infinite looping
    """
    visited = []

    def has_route(origin, destination):
        if origin == destination:
            return True
        visited.append(origin)
        for node in graph[origin]:
            if node not in visited:
                if has_route(node, destination):
                    return True
        return False

    return has_route(first_node, second_node)


class TestRouteBetweenNodes(TestCase):
    def testA(self):
        graph = {1: [2], 2: [3, 4], 3: [], 4: [3, 5], 5: []}
        self.assertEqual(route_between_nodes(graph, 1, 5), True)

    def testB(self):
        graph = {1: [3], 2: [3, 4], 3: [], 4: [3, 5], 5: []}
        self.assertEqual(route_between_nodes(graph, 1, 5), False)


if __name__ == "__main__":
    unittest.main()