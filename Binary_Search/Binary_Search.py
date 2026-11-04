"""
LeetCode 704 - Binary Search
Problem: https://leetcode.com/problems/binary-search/

Approach: Iterative Binary Search

How I Solved It:
1. Initialize left at the first index and right at the last index.
2. Continue while left <= right, so the search includes the
   remaining single-element range.
3. Calculate the middle index.
4. If nums[mid] equals target, return mid.
5. If target is smaller, move right to mid - 1.
6. If target is larger, move left to mid + 1.
7. If the loop finishes without finding the target, return -1.

Key Learning:
Because the input array is sorted, each comparison lets us discard
half of the remaining search range.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left + right)//2
            if nums[mid] == target:
               return mid
            if target < nums[mid]:
                right = mid -1 
            if target > nums[mid]:
                left = mid + 1
        return -1
