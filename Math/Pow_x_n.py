"""
LeetCode 50 - Pow(x, n)
Problem: https://leetcode.com/problems/powx-n/

Approach: Python Exponentiation Operator

How I Solved It:
1. Use Python's exponentiation operator ** with x and n.
2. Return the calculated power.

Key Learning:
Python's ** operator handles positive and negative exponents,
including the edge cases defined by the problem.

Complexity Note:
This delegates exponentiation to Python's numeric implementation.
The exact time and space complexity is implementation-dependent;
this file does not implement an explicit exponentiation algorithm.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
