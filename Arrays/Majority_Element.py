"""
LeetCode 169 - Majority Element
Problem: https://leetcode.com/problems/majority-element/

Approach: Sorting

How I Solved It:
1. Sort the input list.
2. The majority element appears more than n // 2 times.
3. After sorting, all occurrences of the majority element are together.
4. Therefore, the element at index len(nums) // 2 must be the majority element.
5. Return that middle element.

Alternative Approach I Considered:
I also considered using a dictionary to count the frequency of each
number, then selecting the number with the highest frequency. That
approach is kept in the commented code below.

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(n) auxiliary space in the worst case for Python's
list sorting implementation.

"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        x=dict()
        majority=None
        for i in nums:
            if i in x:
                x[i] = x[i]+1
            else:
                x[i]=1
        for i in x:
            if majority==None:
               majority=i
            if x[i] > x[majority]:
               majority=i
        return majority

        '''
        nums.sort()
        return nums[len(nums)//2]
