"""
LeetCode 412 - Fizz Buzz
Problem: https://leetcode.com/problems/fizz-buzz/

Approach: Iterate Through the Numbers and Apply Conditions

How I Solved It:
1. Create a list containing the numbers from 1 to n.
2. Traverse the list using indexes.
3. Check divisibility by both 3 and 5 first:
   - If both divide the number, replace it with "FizzBuzz".
   - Otherwise, if divisible by 3, replace it with "Fizz".
   - Otherwise, if divisible by 5, replace it with "Buzz".
4. Convert each remaining number to a string.
5. Return the list.

Key Learning:
Check the combined condition first. If divisibility by 3 or 5 were
checked first, the FizzBuzz case would be missed.

Time Complexity: O(n)
Space Complexity: O(n) for the output list.
"""

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        x = list(range(1, n + 1))
        for i in range(0,len(x)):
            if x[i]%3==0 and x[i]%5==0:
               x[i]="FizzBuzz"
            elif x[i]%3==0:
                x[i]="Fizz"
            elif x[i]%5==0:
                x[i]="Buzz"
            x[i]=str(x[i])
        return x
