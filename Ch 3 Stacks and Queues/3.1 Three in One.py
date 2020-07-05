""" Cracking the Coding Interview, 6th Edition - Python Solutions
3.1 Three in One: Describe how you could use a single array to implement three stacks.
"""
import unittest
from unittest import TestCase


class ThreeStack:
    """ An object containing three stacks using one array.

    Idea:
    - Store the index of the last top value from the stack in each element in the array so that we can push and pop from
    the respective stacks

    Approach:
    - Keep track of 3 indices, each representing the top index of each stack
    - Every time we push to a stack, the element is a tuple with the value as well as the last top index of the stack
    - Every time we pop from a stack, update the top index and return the popped value
    """
    def __init__(self):
        self.array = []
        self.index_one = None
        self.index_two = None
        self.index_three = None

    def push(self, value, stack):
        last_index = -1
        if stack not in [1, 2, 3]:
            raise Exception('Stack does not exist')

        if stack == 1:
            last_index = self.index_one
        elif stack == 2:
            last_index = self.index_two
        elif stack == 3:
            last_index = self.index_three
        self.array.append((value, last_index))

        if stack == 1:
            self.index_one = len(self.array) - 1
        elif stack == 2:
            self.index_two = len(self.array) - 1
        elif stack == 3:
            self.index_three = len(self.array) - 1
        print(self.array)

    def pop(self, stack):
        last_index = None
        if stack not in [1, 2, 3]:
            raise Exception('Stack does not exist')
        if stack == 1:
            last_index = self.index_one
        elif stack == 2:
            last_index = self.index_two
        elif stack == 3:
            last_index = self.index_three

        if last_index is None:
            return None

        elem = self.array[last_index]
        value = elem[0]
        new_last = elem[1]

        if stack == 1:
            self.index_one = new_last
        elif stack == 2:
            self.index_two = new_last
        elif stack == 3:
            self.index_three = new_last

        return value


class TestThreeInOne(TestCase):
    def testA(self):
        three_stack = ThreeStack()
        three_stack.push('A', 1)
        three_stack.push('D', 2)
        three_stack.push('G', 3)
        three_stack.push('B', 1)
        three_stack.push('E', 2)
        three_stack.push('H', 3)
        three_stack.push('C', 1)
        three_stack.push('F', 2)
        three_stack.push('I', 3)

        self.assertEqual(three_stack.pop(3), 'I')
        three_stack.push('L', 3)
        three_stack.push('O', 3)
        self.assertEqual(three_stack.pop(3), 'O')
        self.assertEqual(three_stack.pop(3), 'L')
        self.assertEqual(three_stack.pop(3), 'H')
        self.assertEqual(three_stack.pop(3), 'G')
        self.assertEqual(three_stack.pop(3), None)

        self.assertEqual(three_stack.pop(2), 'F')
        self.assertEqual(three_stack.pop(2), 'E')
        self.assertEqual(three_stack.pop(2), 'D')
        self.assertEqual(three_stack.pop(2), None)

        three_stack.push('J', 1)
        self.assertEqual(three_stack.pop(1), 'J')
        self.assertEqual(three_stack.pop(1), 'C')
        self.assertEqual(three_stack.pop(1), 'B')
        self.assertEqual(three_stack.pop(1), 'A')


if __name__ == "__main__":
    unittest.main()