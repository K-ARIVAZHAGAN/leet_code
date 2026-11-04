"""
LeetCode 342 - Power of Four
Problem: https://leetcode.com/problems/power-of-four/

Approach: Repeated Division

How I Solved It:
1. First check whether n is positive. Zero and negative numbers
   cannot be powers of four, so return False.
2. While n is divisible by 4, divide it by 4.
3. If n becomes exactly 1, the original number was a power of four.
   Otherwise, it was not.

Why it works:
A positive power of four can be divided by 4 repeatedly until
the result is 1. Any other positive integer will eventually leave
a remainder or finish at a value other than 1.

Time Complexity: O(log_4(n)) for positive n
Space Complexity: O(1)

Note:
My submitted code used n /= 4. In Python, / produces a float.
I used //= here to keep the value as an integer throughout the loop.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1
