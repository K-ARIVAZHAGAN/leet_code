"""
LeetCode 1295 - Find Numbers with Even Number of Digits
Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Approach: Convert Each Number to a String and Check Its Length

How I Solved It:
1. Initialize count to 0.
2. Iterate through every number in nums.
3. Convert the current number to a string.
4. Check whether the number of digits is even using len(i) % 2 == 0.
5. If it is even, increment count.
6. Return count after checking all numbers.

Time Complexity: O(n * d), where n is the number of elements
and d is the maximum number of digits in an element.
Space Complexity: O(d) for the temporary string created during conversion.
"""

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=0
        for i in nums:
            i=str(i)
            if (len(i))%2==0:
                count+=1
        return count
