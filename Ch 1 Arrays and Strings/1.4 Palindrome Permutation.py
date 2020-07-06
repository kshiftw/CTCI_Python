""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""
import unittest
from unittest import TestCase
from collections import Counter


def palindrome_permutation(string: str) -> bool:
    """ Check if a given string is a permutation of a palindrome

    Idea: A palindrome consists of two variations:
    1) All characters have an even number of occurrences.
        ex: 'abba' -> {'a': 2, 'b': 2}
    2) All characters have an even number of occurrences except for 1 character that has an odd number of occurrences
        ex. 'aabcccbaa' -> {'a': 4, 'b': 2, 'c': 3}
    If there is more than one character that has an odd number of occurrences, then it cannot be a palindrome.

    Complexity:
    - Time: O(N) - need to loop through all N characters in string
    - Space: O(N) - dictionary will store at most N elements if all characters are unique

    Approach:
    - Use Counter to get count of characters in the string
    - Loop through the character counts and keep track of how many odd_counts there are
    - If we find more than 1 odd_count, then it cannot be a permutation of a palindrome, return False.
    - If we do not find more than 1 odd_count, return True.
    """
    char_count = Counter(string)
    odd_count = 0
    
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True
            

class TestPalindromePermutation(TestCase):
    def testA(self):
        actual = palindrome_permutation('joker')
        expected = False
        self.assertEqual(actual, expected)

    def testB(self):
        actual = palindrome_permutation('ratroot')
        expected = True
        self.assertEqual(actual, expected)

    def testC(self):
        actual = palindrome_permutation('yakka')
        expected = True
        self.assertEqual(actual, expected)

    def testD(self):
        actual = palindrome_permutation('yakkkaay')
        expected = False
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()