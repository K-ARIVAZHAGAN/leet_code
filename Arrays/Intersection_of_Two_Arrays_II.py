"""
LeetCode 350 - Intersection of Two Arrays II
Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Approach: Frequency Dictionary (Hash Map)

How I Solved It:
1. Create a dictionary to store how many times each number appears in nums1.
2. Traverse nums1 and increment the frequency of each number.
3. Traverse nums2 and check whether the current number exists in the
   dictionary with a remaining frequency greater than zero.
4. If it does, add the number to the result and decrease its frequency.
5. Return the result.

Why the frequency check matters:
It ensures that each number appears in the result only as many times
as it appears in both input arrays.

Time Complexity: O(n + m) on average, where n and m are the
lengths of nums1 and nums2.
Space Complexity: O(u + k), where u is the number of distinct
values stored in the dictionary and k is the result length.
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n1={}
        res=[]
        for i in nums1:
            if i in n1:
                n1[i]=n1[i]+1
            else:
                n1[i]=1
        for i in nums2:
           if i in n1 and n1[i] > 0:
            res.append(i)
            n1[i] -=1
        return res
