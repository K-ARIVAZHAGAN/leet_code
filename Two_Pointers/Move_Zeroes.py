"""
LeetCode 283 - Move Zeroes
Problem: https://leetcode.com/problems/move-zeroes/

Approach: Two Pointers (In-place Swapping)

How I Solved It:
1. Initialize index = 0 to mark the next position for a non-zero value.
2. Traverse the array using i.
3. Whenever nums[i] is not zero, swap nums[i] with nums[index].
4. Move index one position forward.
5. After the traversal, all non-zero values remain in their
   original relative order, followed by the zeroes.

Key Learning:
The index pointer tracks where the next non-zero element belongs.
Swapping in-place avoids creating another array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        index=0
        for i in range(len(nums)):
           if nums[i]!=0:
              nums[index],nums[i]=nums[i],nums[index]
              index +=1
