"""
LeetCode 268 - Missing Number
Problem: https://leetcode.com/problems/missing-number/

Approach: Arithmetic Sum Formula

How I Solved It:
1. Let n be the length of nums. The expected values are from 0 to n.
2. Calculate the expected sum using n * (n + 1) // 2.
3. Subtract the actual sum of nums.
4. The difference is the missing number.

Key Learning:
The sum formula avoids checking each possible number individually
or creating an additional set.

Time Complexity: O(n), because sum(nums) traverses the list.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
