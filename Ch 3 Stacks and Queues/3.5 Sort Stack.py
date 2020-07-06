""" Cracking the Coding Interview, 6th Edition - Python Solutions
3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
"""
import unittest
from unittest import TestCase


def sort_stack(stack):
    """ Sort a stack using only an additional temporary stack.

    Idea:
    - Use temporary stack to store all elements in reversed sorting order (largest on top)

    Complexity:
    - Time: O(N^2) - for each element, we will need to compare it against all other elements to determine which one is
    larger
    - Space: O(N) - need an additional stack that will store all elements in reversed sorted order

    Approach:
    - Pop each element from the stack
        - If element is larger than the top of the temporary stack, then push it to the top
        - If element is smaller than top of temporary stack, determine where it fits by moving all larger elements to
        the original stack
            - On the next loop of the outer while loop, we will simply move all larger elements back to the temporary
            stack because they are already in the correct order 
    """
    if stack.is_empty():
        return
    temp_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)

    # temp stack is sorted, but in reverse order (largest value on top), so we push all values back into the original
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def get_stack(self):
        return self.stack


class TestSortStack(TestCase):
    def testA(self):
        stack = Stack()
        stack.push(5)
        stack.push(1)
        stack.push(4)
        stack.push(8)
        stack.push(7)

        sort_stack(stack)
        self.assertEqual(stack.get_stack(), [8, 7, 5, 4, 1])

    def testB(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)

        sort_stack(stack)
        self.assertEqual(stack.get_stack(), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()