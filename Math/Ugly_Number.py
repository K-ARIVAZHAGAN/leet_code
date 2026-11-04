"""
LeetCode 263 - Ugly Number
Problem: https://leetcode.com/problems/ugly-number/

Approach: Repeatedly Divide by Allowed Prime Factors

How I Solved It:
1. If n is zero or negative, return False.
2. Check the prime factors 2, 3, and 5 one at a time.
3. While n is divisible by the current factor, divide n by it.
4. After removing all factors of 2, 3, and 5, check whether n is 1.
5. If it is 1, the original number had no prime factors other than
   2, 3, and 5, so return True. Otherwise, return False.

Time Complexity: O(log n) for positive n.
Space Complexity: O(1).
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p

        return n == 1
