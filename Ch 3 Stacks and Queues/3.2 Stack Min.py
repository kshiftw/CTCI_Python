""" Cracking the Coding Interview, 6th Edition - Python Solutions
3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
import unittest
from unittest import TestCase


class StackMin:
    """ A stack that also returns the minimum element.

    Idea:
    - Keep track of the previous minimum value

    Approach:
    - For each push, add a tuple containing the added value as well as the last minimum value of the stack
    - When popping, take the second element of the tuple and set that as the last minimum value
    """
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, value):
        if self.min is None:
            self.min = value

        self.stack.append((value, self.min))

        if value <= self.min:
            self.min = value

    def pop(self):
        elem = self.stack.pop(-1)
        value = elem[0]
        self.min = elem[1]
        return value

    def get_min(self):
        return self.min

    def print_stack(self):
        print(self.stack)


class TestStackMin(TestCase):
    def testA(self):
        stack = StackMin()
        stack.push(8)
        stack.push(7)
        stack.push(6)
        stack.push(5)

        stack.print_stack()
        self.assertEqual(stack.get_min(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.get_min(), 6)

        stack.push(9)
        stack.push(1)
        self.assertEqual(stack.get_min(), 1)
        stack.print_stack()

    def testB(self):
        stack = StackMin()
        stack.push(6)
        stack.push(10)
        stack.push(3)
        stack.push(5)
        stack.push(7)

        stack.print_stack()
        self.assertEqual(stack.get_min(), 3)
        stack.pop()
        self.assertEqual(stack.get_min(), 3)
        stack.pop()
        self.assertEqual(stack.get_min(), 3)
        stack.pop()
        self.assertEqual(stack.get_min(), 6)
        stack.print_stack()


if __name__ == "__main__":
    unittest.main()