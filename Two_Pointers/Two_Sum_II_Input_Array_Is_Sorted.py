"""
LeetCode 167 - Two Sum II - Input Array Is Sorted
Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Approach: Two Pointers

How I Solved It:
1. Place one pointer at the beginning and another at the end.
2. Add the values at both pointer positions.
3. If their sum equals target, return their positions using
   1-based indexing as required by the problem.
4. If the sum is smaller than target, move the left pointer right
   to increase the sum.
5. Otherwise, move the right pointer left to decrease the sum.
6. Continue until the pair is found.

Key Learning:
Because the array is sorted, moving the left pointer increases
the possible sum, while moving the right pointer decreases it.

Time Complexity: O(n)
Space Complexity: O(1)

Note: The problem guarantees exactly one solution.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
       i=0
       j=len(numbers)-1
       while i < len(numbers):
         total=numbers[i]+numbers[j]
         if total == target:
            return [i+1,j+1]
         elif total <target:
            i+=1
         else:
            j-=1
