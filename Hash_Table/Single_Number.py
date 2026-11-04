"""
LeetCode 136 - Single Number
Problem: https://leetcode.com/problems/single-number/

Approach: Set + Sum Difference

How I Solved It:
1. Convert nums into a set to keep only distinct values.
2. Sum the unique values.
3. Multiply that sum by 2.
4. Subtract the sum of the original list.
5. The result is the number that appears only once, because every
   other value appears twice in the original list.

Formula:
2 * sum(set(nums)) - sum(nums)

Time Complexity: O(n) average.
Space Complexity: O(n) for the set.
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int: 
       return 2 * sum(set(nums))-sum(nums)
