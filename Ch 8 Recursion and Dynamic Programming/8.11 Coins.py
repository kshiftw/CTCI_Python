""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.11 Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""
import unittest
from unittest import TestCase


def coins(n: int) -> int:
    """ Counts number of ways to represent n coins.

    Idea:
    - From the largest denomination to the smallest:
        - From 0 to however many times the denomination can make up the amount, recursively calculate the same thing but
        with a smaller denomination
    - Once we reach 1 cent, we have reached the end b/c there are no smaller denominations and there is only one
    remaining combination to use 1 cent towards the remainder amount

    Approach:
    - Use a while loop to calculate how many times a denomination can go into making up the amount
        - For each way, call change() with the remainder amount
        - Recursion ends with 1 cent denomination
    """
    coins_list = [25, 10, 5, 1]

    def change(amount, index):
        if index >= len(coins_list) - 1:
            return 1
        denomination = coins_list[index]
        count_ways = 0
        i = 0
        next_denomination = 0
        while next_denomination <= amount:
            remainder = amount - next_denomination
            count_ways += change(remainder, index + 1)
            i += 1
            next_denomination = i * denomination
        return count_ways

    return change(n, 0)


class TestCoins(TestCase):
    def testA(self):
        self.assertEqual(coins(5), 2)
        self.assertEqual(coins(30), 18)


if __name__ == "__main__":
    unittest.main()