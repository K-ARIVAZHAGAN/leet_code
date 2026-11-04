"""
LeetCode 796 - Rotate String
Problem: https://leetcode.com/problems/rotate-string/

Approach: String Concatenation and Substring Check

How I Solved It:
1. Check whether s and goal have the same length.
   If not, return False because rotation cannot change string length.
2. Concatenate s with itself.
3. Check whether goal is contained in the concatenated string.
4. Return the membership result.

Why it works:
Every cyclic rotation of s appears as a substring of s + s
with the same length as s.

Time Complexity: O(n) expected for the substring search in typical
implementations; exact behavior depends on the string-search algorithm.
Space Complexity: O(n) for s + s.
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return goal in (s+s)
