"""
LeetCode 231 - Power of Two
Problem: https://leetcode.com/problems/power-of-two/

Approach: Generate Powers of Two and Compare

How I Solved It:
1. Initialize numbers = 0 to represent the exponent.
2. While the current power of two is not greater than n:
   - Check whether 2 ** numbers equals n.
   - If it does, return True.
   - Otherwise, increase the exponent.
3. If no power matches, return False.

Complexity Note:
This implementation repeatedly calculates 2 ** numbers.
There are O(log n) iterations for positive n, and each exponentiation
has a cost that depends on the integer implementation and operand size.
Space usage is O(1) auxiliary, excluding integer representation details.

Edge Case:
For n <= 0, the loop does not execute and the method returns False.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        numbers = 0

        while n >= 2**numbers:
            if 2**numbers == n:
                return True
            
            numbers += 1
        
        return False
