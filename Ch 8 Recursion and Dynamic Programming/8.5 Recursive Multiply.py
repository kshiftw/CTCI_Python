""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.5 Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.
"""
import unittest
from unittest import TestCase


def recursive_multiply(a: int, b: int) -> int:
    """ Calculate the product of two positive integers.

    Assumption:
    - a and b are unique positive integers

    Idea:
    - Break down the problem by recursively calculating half of the product

    Complexity:
    - Time: O(log(N)) - N is the smaller of two numbers. N is divided by 2 every time helper is called.
    - Space: O(log(N)) - call stack for helper function

    Approach:
    - First determine which integer is smaller
    - Recursively call helper until small is either 0 or 1
        - the bit shift will act like integer division
        - Determine if small is odd or even
    """
    smaller = a if a < b else b
    bigger = a if a > b else b

    def helper(small, big):
        if small == 0:
            return 0
        if small == 1:
            return big

        half_small = small >> 1
        half_product = helper(half_small, big)

        if small % 2 == 0:
            return half_product + half_product
        else:
            return half_product + half_product + big

    return helper(smaller, bigger)


class TestRecursiveMultiply(TestCase):
    def testA(self):
        self.assertEqual(recursive_multiply(5, 6), 30)
        self.assertEqual(recursive_multiply(4, 7), 28)
        self.assertEqual(recursive_multiply(9, 21), 189)


if __name__ == "__main__":
    unittest.main()