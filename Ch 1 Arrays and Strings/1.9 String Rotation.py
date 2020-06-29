""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""
import unittest
from unittest import TestCase


def string_rotation(s1: str, s2: str) -> bool:
    """ Check if s2 is a rotation of s1.

    Idea:
    - The two strings must be equal length to be rotations
    - From the beginning of s1, find its longest substring that is also a substring of s2
    - The remaining substring of s1 must also be a substring of s2 if s2 is a rotation of s1
    Ex. s1 = helloworld, s2 = rldhellowo
        - 'hellowo' in s1 is a substring of s2
        - the remaining substring of s1 'rld' must also be a substring of s2

    Approach:
    - Loop through s1 until we find the longest common substring with s2
    - Check if the remaining substring of s1 is also a substring of s2

    Alternative:
    - Notice that if s2 is a rotation of s1, then s2 MUST be a substring of s1 concatenated with itself
        Ex. s1 = joke, s2 = kejo
        If s2 is a rotation, then it must be substring of s1+s1 = jokejoke
    """
    if len(s1) != len(s2) or s1 == s2:
        return False

    index = 0
    while index < len(s1):
        substring = s1[:index + 1]
        if substring not in s2:
            remaining = s1[index + 1:]
            break
        else:
            index += 1
    if remaining in s2:
        return True
    else:
        return False


class TestStringRotation(TestCase):
    def testA(self):
        actual = string_rotation('waterbottle', 'erbottlewat')
        expected = True
        self.assertEqual(actual, expected)

    def testB(self):
        actual = string_rotation('waterbottlr', 'erbottlewat')
        expected = False
        self.assertEqual(actual, expected)

    def testC(self):
        actual = string_rotation('waterbot', 'erbottlewat')
        expected = False
        self.assertEqual(actual, expected)

    def testD(self):
        actual = string_rotation('waterbottle', 'ewaterbottl')
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()