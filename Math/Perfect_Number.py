"""
LeetCode 507 - Perfect Number
Problem: https://leetcode.com/problems/perfect-number/

Approach: Check Divisors up to the Square Root

How I Solved It:
1. Numbers less than or equal to 1 cannot be perfect, so return False.
2. Start total at 1 because 1 is a proper divisor of every
   positive integer greater than 1.
3. Start checking possible divisors from 2.
4. Continue while i * i <= num.
5. If num is divisible by i:
   - Add i to the divisor sum.
   - Add its paired divisor num // i, unless it is the same
     divisor (which happens for a perfect square).
6. Move to the next possible divisor.
7. Return whether the sum of proper divisors equals num.

Key Learning:
Divisors come in pairs: i and num // i. Checking only up to
the square root avoids scanning all numbers up to num.

Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

            i += 1

        return total == num
