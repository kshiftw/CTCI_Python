""" Cracking the Coding Interview, 6th Edition - Python Solutions
8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""
import unittest
from unittest import TestCase


def triple_step_recursive(num_steps: int) -> int:
    """ Calculate the number of possible ways to reach n steps.

    Idea:
    - Tribonnaci numbers
    - At each step, n, there are 3 ways to get there.
        - We are at step n - 1 and we hop 1 step
        - We are at step n - 2 and we hop 2 steps
        - We are at step n - 3 and we hop 3 steps
        - Therefore, the number of ways to get to n can be represented with f(n) = f(n - 1) + f(n - 2) + f(n - 3)
    - Base case:
        - If we are at step 0, we consider it to have 1 possible way to get there

    Complexity:
    - Time: O(N) - need the calculate the possible ways for each number from 1 to N
    - Space: O(N) - need to store up to N values in the memo dictionary

    Approach:
    - Use memoization to avoid redundant function calls and avoid exponential time complexity O(3^N)
    """
    memo = {}

    def triple_step(n):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            result = 1
        elif n == 2:
            result = 2
        else:
            result = triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)
        memo[n] = result
        return result

    return triple_step(num_steps)


def triple_step_iterative(num_steps: int) -> int:
    dp = [1, 1, 2]
    for x in range(3, num_steps + 1):
        dp.append(dp[x - 1] + dp[x - 2] + dp[x - 3])
    return dp[num_steps]


class TestTripleStep(TestCase):
    def testA(self):
        self.assertEqual(triple_step_recursive(4), 7)
        self.assertEqual(triple_step_recursive(8), 81)

    def testB(self):
        self.assertEqual(triple_step_iterative(4), 7)
        self.assertEqual(triple_step_iterative(8), 81)


if __name__ == "__main__":
    unittest.main()