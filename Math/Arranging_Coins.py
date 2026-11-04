"""
LeetCode 441 - Arranging Coins
Problem: https://leetcode.com/problems/arranging-coins/

Approach: Iterative Subtraction

How I Solved It:
1. Start with row number i = 1.
2. Subtract i coins from n to fill the current row.
3. Check whether the remaining coins are enough to fill the next row.
4. If they are not enough, stop.
5. Otherwise, move to the next row and repeat.
6. Return the number of completely filled rows.

Note:
This implementation follows the problem's constraint that n is positive.

Time Complexity: O(sqrt(n)), because the number of coins used
to fill k complete rows is 1 + 2 + ... + k.
Space Complexity: O(1).
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while i < n:
            n = n - i
            if n - (i+1) < 0:
                break
            i=i+1
               
        return i
