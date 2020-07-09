""" Cracking the Coding Interview, 6th Edition - Python Solutions
4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""
import unittest
from unittest import TestCase


def build_order(projects: list, dependencies: list) -> list:
    """ Generates the build order that allows projects to be built.

    Idea:
    - Topological Sort
        - Continuously find projects with zero dependencies and remove their outgoing links
        - No valid build order if there is a cycle 

    Complexity:
    - Time: O(V + E) - where V is the number of vertices (projects) and E is the number of edges (dependencies)
        - Need to navigate through every node and link
    - Space: O(V + E) - need to store each node as well as its edges

    Approach:
    1) Build a graph (represented by an adjacency list) using the projects list and dependencies list given
    2) Find the projects with no dependencies -> these can be started right away
        - Add them to the queue
    3) Remove all outgoing links from these projects b/c completing these projects means that their dependents can
    also be completed
        - Add the project to the build order
    4) Repeat steps 2 and 3 until queue is empty
    5) If there is a cycle in the graph, then there is no valid build order because two dependencies will depend on
    each other to complete before each starts, which is not possible
    """
    nodes = {}
    queue = []
    order_list = []
    for project in projects:
        nodes[project] = Node(project)
    for dependency in dependencies:
        nodes[dependency[0]].add_edge(nodes[dependency[1]])
    for project in projects:
        if nodes[project].dependencies_count == 0:
            queue.append(project)
    while queue:
        project = queue.pop(0)
        order_list.append(project)
        for dependent in nodes[project].edges:
            dependent.dependencies_count -= 1
            if dependent.dependencies_count == 0:
                queue.append(dependent.value)
    if len(order_list) < len(projects):
        return None
    return order_list


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.dependencies_count = 0

    def add_edge(self, node):
        self.edges.append(node)
        node.dependencies_count += 1


class TestBuildOrder(TestCase):
    def testA(self):
        projects = ['A', 'B', 'C', 'D', 'E', 'F']
        dependencies = [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C')]
        self.assertEqual(build_order(projects, dependencies), ['E', 'F', 'B', 'A', 'D', 'C'])

    def testB(self):
        projects = ['A', 'B', 'C', 'D', 'E', 'F']
        dependencies = [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C'), ('C', 'F')]
        self.assertEqual(build_order(projects, dependencies), None)

    def testC(self):
        projects = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        dependencies = [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C'), ('G', 'H'), ('G', 'B')]
        self.assertEqual(build_order(projects, dependencies), ['E', 'F', 'G', 'A', 'H', 'B', 'D', 'C'])


if __name__ == "__main__":
    unittest.main()