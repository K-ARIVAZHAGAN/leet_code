"""
LeetCode 69 - Sqrt(x)
Problem: https://leetcode.com/problems/sqrtx/

Approach: Linear Search for the Integer Square Root

How I Solved It:
1. If x is less than 2, return x directly.
2. Set mid to x // 2, since the integer square root is no greater
   than x // 2 for x >= 2.
3. Check candidate values from 0 through mid.
4. Whenever i * i is less than or equal to x, store i as the
   current answer.
5. Stop when i * i becomes greater than x.
6. Return the largest valid candidate found.

Complexity Note:
The loop checks up to about x / 2 candidates, so time complexity
is O(x). The solution uses O(1) auxiliary space.

Note:
The original code uses int(x / 2). This is kept as submitted.
Using x // 2 would avoid floating-point conversion for large integers.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        mid = int(x / 2)
        sqrt = 0
        if x < 2:
            return x
        else :
            
            for i in range(0, mid + 1):
                if i * i <= x:
                    sqrt = i
                else:
                    break
        return sqrt
