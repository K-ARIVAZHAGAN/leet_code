"""
LeetCode 217 - Contains Duplicate
Problem: https://leetcode.com/problems/contains-duplicate/

Approach: Set and Length Comparison

How I Solved It:
1. Convert nums into a set.
2. A set stores only unique values, removing duplicates.
3. Compare the length of the original list with the length of the set.
4. If the lengths differ, at least one duplicate existed.
5. Return the result of that comparison.

Time Complexity: O(n) average.
Space Complexity: O(n) for the set.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
