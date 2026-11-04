"""
LeetCode 202 - Happy Number
Problem: https://leetcode.com/problems/happy-number/

Approach: Cycle Detection with a Set

How I Solved It:
1. Create a set to remember numbers already visited.
2. Continue until n becomes 1.
3. If n is already in the set, a cycle has formed, so return False.
4. Add n to the set.
5. Calculate the sum of the squares of its digits:
   - Convert n to a string to iterate through its digits.
   - Convert each digit back to an integer and square it.
6. Replace n with the calculated total and repeat.
7. If n reaches 1, return True.

Key Learning:
A set helps detect repeated states. If a number repeats before reaching 1,
the process will loop forever.

Time Complexity: O(log n) per transformation; the number of distinct
states before reaching 1 or repeating is bounded for this process.
Space Complexity: O(k) for the set of visited values, where k is the
number of transformations before termination.

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            total = 0

            for digit in str(n):
                total += int(digit) ** 2

            n = total

        return True
