"""
LeetCode 27 - Remove Element
Problem: https://leetcode.com/problems/remove-element/

Approach: Copy the List, Then Remove Matching Values

How I Solved It:
1. Make a copy of nums so that iterating over the copy is not affected
   when values are removed from the original list.
2. Traverse the copied values.
3. Whenever a value equals val, remove one occurrence of it from nums.
4. Return the new length of nums.

Important Complexity Note:
List.remove() searches for the value and shifts later elements.
Repeated removals can make this implementation O(n^2) in the worst case.
The copied list uses O(n) extra space.

The LeetCode judge checks the first k elements, where k is the returned
length. The remaining elements do not matter.
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        x=nums.copy()
        for i in x:
            if i == val:
                nums.remove(i)
               
        return len(nums)
