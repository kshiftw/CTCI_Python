""" Cracking the Coding Interview, 6th Edition - Python Solutions
3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""
import unittest
from unittest import TestCase


class MyQueue:
    """ A queue implemented using two stacks

    Idea:
    - When we pop and push elements from one stack to another, the elements are reversed, which is in the order that
    we need to pop from a queue

    Approach:
    - Use two stacks, one for pushing elements onto, and another for storing the next elements to pop
    - Pushing to the queue is straightforward and similar to pushing to a stack
    - When we pop for the first time, we pop all elements from the push_stack and push them into the pop_stack
        - This makes them in the reverse order (ie. FIFO) that is needed for queue popping
        - If we pop again, we need to check if we still have elements in the pop_stack
        - We only repopulate the pop_stack if we have already popped all elements out of it
    """
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, value):
        self.push_stack.push(value)

    def pop(self):
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def print_stacks(self):
        print(self.push_stack.print_stack(), self.pop_stack.print_stack())


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def print_stack(self):
        return self.stack


class TestMyQueue(TestCase):
    def testA(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.push(4)
        queue.push(5)

        queue.print_stacks()

        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        queue.push(6)
        queue.push(7)
        self.assertEqual(queue.pop(), 4)

        queue.print_stacks()


if __name__ == "__main__":
    unittest.main()