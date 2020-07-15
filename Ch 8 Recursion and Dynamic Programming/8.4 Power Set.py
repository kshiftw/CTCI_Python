""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.4 Power Set: Write a method to return all subsets of a set.
"""
import unittest
from unittest import TestCase


def power_set(input_set):
    """ Generates all subsets of a set.

    From: https://github.com/w-hat/ctci-solutions/blob/master/ch-08-recursion-and-dynamic-programming/04-power-set.py

    Idea:
    - Recursively build the subsets from empty set and include one element at a time
    - Recognize the pattern that with each new element, the new powerset is double the size of the previous powerset
    where all previous subsets are cloned and added with the new element
        P1 = {}, {'a'}
        P2 = {}, {'a'}, {'b'}, {'a', 'b'}
        P3 = {}, {'a'}, {'b'}, {'a', 'b'}, {'c'}, {'a', 'c'}, {'b', 'c'}, {'a', 'b', 'c'}
        P4 = {}, {'a'}, {'b'}, {'a', 'b'}, {'c'}, {'a', 'c'}, {'b', 'c'}, {'a', 'b', 'c'},
            {'d'}, {'a', 'd'}, {'b', 'd'}, {'a', 'b', 'd'}, {'c', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'},
            {'a', 'b', 'c', 'd'}

    Complexity:
    - Time: O(N * 2^N) - from empty to including N elements, we need to iterate through all the subsets we previously
    create
    - Space: O(N * 2^N) - store all subsets

    Approach:
    - use frozenset for their immutability - we cannot create a set of sets because the sets are mutable and set
    elements can only be immutable
    """
    ps = {frozenset()}
    for element in input_set:
        additions = set()
        for subset in ps:
            additions.add(subset.union(element))
        ps = ps.union(additions)
    return ps


class TestPowerSet(TestCase):
    def testA(self):
        test_set = {'a', 'b', 'c', 'd'}
        ps = power_set(test_set)
        self.assertEqual(len(ps), 16)


if __name__ == "__main__":
    unittest.main()