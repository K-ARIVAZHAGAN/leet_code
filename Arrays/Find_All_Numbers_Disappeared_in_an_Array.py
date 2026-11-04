"""
LeetCode 448 - Find All Numbers Disappeared in an Array
Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Approach: Set Lookup

How I Solved It:
1. Convert nums into a set. This keeps the unique values and allows
   efficient membership checks.
2. Create an empty result list.
3. Iterate through every integer from 1 to len(nums), inclusive.
4. If the current integer is not in the set, add it to the result.
5. Return the result containing all missing numbers.

Time Complexity: O(n) on average, because building the set and
checking the range both take linear time.
Space Complexity: O(n) for the set, excluding the output list.

Key Learning:
A set is useful when we need to check quickly whether a value
exists in a collection.
"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_set=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                res.append(i)
        return res
