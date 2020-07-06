""" Cracking the Coding Interview, 6th Edition - Python Solutions
3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
"""
import unittest
from unittest import TestCase


class StackPlates:
    """ An object containing a set of stacks each with a limited size based on the threshold value given.

    Idea:
    - Keep a count of the number of elements in the set and use it to determine when to create a new stack
    - Have a list of stacks (ie. self.stacks) to easily reference the individual stacks

    Approach:
    - When pushing, if we have reached the size limit for a single stack (ie. elem_count % threshold == 0) then we
    should create a new stack
    - When popping, if we have popped out the last element of a stack, also pop the stack from stacks
    """
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []
        self.elem_count = 0

    def push(self, value):
        if self.elem_count % self.threshold == 0:
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)
        self.elem_count += 1

    def pop(self):
        if self.elem_count == 0:
            return None
        self.elem_count -= 1
        if self.elem_count % self.threshold == 0:
            value = self.stacks[-1].pop()
            self.stacks.pop()
        else:
            value = self.stacks[-1].pop()
        return value

    def print_stacks(self):
        print(self.stacks)


class TestStackPlates(TestCase):
    def testA(self):
        stacks = StackPlates(3)
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        stacks.push(5)
        stacks.push(6)
        stacks.push(7)

        stacks.print_stacks()

        self.assertEqual(stacks.pop(), 7)
        stacks.print_stacks()
        self.assertEqual(stacks.pop(), 6)
        self.assertEqual(stacks.pop(), 5)
        self.assertEqual(stacks.pop(), 4)
        self.assertEqual(stacks.pop(), 3)
        stacks.push(8)
        stacks.push(9)
        stacks.push(10)

        stacks.print_stacks()

    def testB(self):
        stacks = StackPlates(2)
        stacks.push(1)
        stacks.push(2)
        stacks.push(3)

        stacks.print_stacks()

        self.assertEqual(stacks.pop(), 3)
        self.assertEqual(stacks.pop(), 2)
        self.assertEqual(stacks.pop(), 1)
        self.assertEqual(stacks.pop(), None)
        self.assertEqual(stacks.pop(), None)

        stacks.push('A')
        stacks.push('B')
        stacks.push('C')
        stacks.print_stacks()


if __name__ == "__main__":
    unittest.main()