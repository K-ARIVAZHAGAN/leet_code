"""
LeetCode 374 - Guess Number Higher or Lower
Problem: https://leetcode.com/problems/guess-number-higher-or-lower/

Approach: Binary Search Using the guess API

How I Solved It:
1. Set the search range from 1 to n.
2. Calculate the middle number.
3. Call guess(mid):
   - 0 means the correct number was found, so return mid.
   - -1 means mid is higher than the picked number, so search left.
   - 1 means mid is lower than the picked number, so search right.
4. Repeat until the correct number is found.

Key Learning:
The API tells us which half of the range can be discarded,
so binary search finds the answer efficiently.

Time Complexity: O(log n)
Space Complexity: O(1)

Note:
The guess() API is provided by LeetCode; it is not defined in this file.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
              mid = ( left + right ) // 2
              result = guess(mid)
              if result == 0 :
                return mid
              elif result  == -1 :
                right = mid - 1
              else:
                left = mid + 1
