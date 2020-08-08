""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.9 Parens: Implement an algorithm to print all valid (Le., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())) , (()()), (())(), ()(()), ()()()
"""
import unittest
from unittest import TestCase


def parens(n: int) -> list:
    """ Generate all valid combinations of n pairs of parentheses.

    Algorithm taken from the book's solution.

    Idea:
    - Keep track of how many left and right parentheses need to be added
        - Recursively add parentheses until base cases

    Complexity:
    - Time: O(N * Cat(N))
        See: https://stackoverflow.com/questions/37385964/time-complexity-for-combination-of-parentheses

    Approach:
    - Base cases:
        - If we have used up more closing (right) parentheses than opening (left) parentheses, it is invalid
        - If we have used up all left and right parentheses, it is a valid combination - add it to the combo list
    - Recursively add left parentheses
        - Recursively add right parentheses
    """
    parens_list = []

    def next_parens(left_remain, right_remain, string):
        if right_remain < left_remain:
            return
        if left_remain == 0 and right_remain == 0:
            parens_list.append(string)
            return

        if left_remain:
            parens(left_remain - 1, right_remain, string + "(")
            
        if right_remain:
            parens(left_remain, right_remain - 1, string + ")")

    next_parens(n, n, "")
    return parens_list


class TestParens(TestCase):
    def testA(self):
        self.assertEqual(parens(3), ["((()))", "(()())", "(())()", "()(())",
                                     "()()()"])
        self.assertEqual(parens(2), ["(())", "()()"])


if __name__ == "__main__":
    unittest.main()
