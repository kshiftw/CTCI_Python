""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""
import unittest
from unittest import TestCase


def one_away(string_one: str, string_two: str) -> bool:
    """ Check if two strings are zero or one edit away from each other.

    Idea: Compare the two strings for the three scenarios:
    1) Equal length - compare all characters and see if there are any mismatches
    2) Unequal length (combine insert character and remove character into one check)
        - Check shorter string and see if every character is equal to the longer string except for one character

    Complexity:
    - Time: O(M+N) - need to loop through the M characters of string_one and N characters of string_two
    - Space: O(1) - constant space to store comparison variables

    Approach:
    - Compare the two string lengths
    - If there is a length difference of more than two characters, return False
    - If the two strings are equal, return True
    - If the strings have equal lengths, check if there is more than one character difference
    - If the strings have unequal lengths, determine which one is the shorter vs longer string
        - If we see a mismatch, keep track of it using the shift variable
            - If the second character is also a mismatch, ie. 'abc' and 'abdf', then there needs to be more than one
            edit to make the strings equal, return False
            - If we see a mismatch again, return False
    """
    length_one = len(string_one)
    length_two = len(string_two)
    equal_length_diff = 0

    if abs(length_one - length_two) > 1:
        return False
    if string_one == string_two:
        return True
    if length_one == length_two:
        for index in range(length_one):
            if string_one[index] != string_two[index]:
                equal_length_diff += 1
            if equal_length_diff > 1:
                return False
        return True
    else:
        if length_one > length_two:
            short = string_two
            long = string_one
        else:
            short = string_one
            long = string_two
        shift = 0
        for index in range(len(short)):
            if short[index] != long[index + shift]:
                if shift == 1 or short[index] != long[index + 1]:
                    return False
                shift = 1
        return True


class TestOneAway(TestCase):
    def testA(self):
        actual = one_away('joker', 'jokefr')
        expected = True
        self.assertEqual(actual, expected)

    def testB(self):
        actual = one_away('joker', 'jokedd')
        expected = False
        self.assertEqual(actual, expected)

    def testC(self):
        actual = one_away('jakap', 'joke')
        expected = False
        self.assertEqual(actual, expected)

    def testD(self):
        actual = one_away('joke', 'joke')
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()