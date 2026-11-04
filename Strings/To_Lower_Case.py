"""
LeetCode 709 - To Lower Case
Problem: https://leetcode.com/problems/to-lower-case/

Approach: Python Built-in String Method

How I Solved It:
1. Use Python's lower() string method.
2. Return the converted string.

Key Learning:
Python strings provide lower() to convert uppercase characters
to their lowercase equivalents. Characters that are not uppercase
letters remain unchanged.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(n) for the returned string.
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
