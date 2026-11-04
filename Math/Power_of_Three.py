"""
LeetCode 326 - Power of Three
Problem: https://leetcode.com/problems/power-of-three/

Approach: Repeated Division

How I Solved It:
1. If n is zero or negative, return False.
2. While n is divisible by 3, divide it by 3 using integer division.
3. After removing all factors of 3, check whether n equals 1.
4. If it does, the original number was a power of three.

Time Complexity: O(log_3(n)) for positive n.
Space Complexity: O(1).
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        while n%3==0:
            n=n//3
        return n==1
