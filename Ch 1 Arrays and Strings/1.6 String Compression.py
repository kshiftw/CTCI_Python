""" Cracking the Coding Interview, 6th Edition - Python Solutions
1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
import unittest
from unittest import TestCase


def string_compression(string: str) -> str:
    """ Compress a string into a character + count sequence.

    Idea:
    - Although we want character counts, a dictionary here is not useful because it doesn't help with returning the same
    order of characters in the string
    - We can maintain order by looping through the string and comparing each character with the previous character

    Approach:
    - Loop through the string and compare the current character with the previously saved character
        - If it is the same, increase the count
        - If they are not the same, append the result string with the character + count sequence and save the character
    """
    if not string:
        return ""

    index = 1
    count = 1
    result_str = ""
    save_char = string[0]

    while index < len(string):
        if string[index] == save_char:
            count += 1
        else:
            result_str += save_char + str(count)
            save_char = string[index]
            count = 1
        index += 1

    result_str += save_char + str(count)
    return result_str


class TestOneAway(TestCase):
    def testA(self):
        actual = string_compression('joker')
        expected = "j1o1k1e1r1"
        self.assertEqual(actual, expected)

    def testB(self):
        actual = string_compression('aabcccccaaa')
        expected = "a2b1c5a3"
        self.assertEqual(actual, expected)

    def testC(self):
        actual = string_compression('')
        expected = ""
        self.assertEqual(actual, expected)

    def testD(self):
        actual = string_compression('Jjarbiiinks')
        expected = "J1j1a1r1b1i3n1k1s1"
        self.assertEqual(actual, expected)

    def testE(self):
        actual = string_compression('X')
        expected = "X1"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()