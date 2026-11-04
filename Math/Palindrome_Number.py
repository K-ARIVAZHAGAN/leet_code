# 9. Palindrome Number

**LeetCode:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)  
**Topic:** Math  
**Difficulty:** Easy

## My Approach

I first handle negative numbers because a negative number cannot be a palindrome.

Then I:
1. Convert the number into a string.
2. Build a reversed string by iterating from the last character to the first.
3. Convert the reversed string back into an integer and compare it with the original number.

If both values are equal, the number is a palindrome.

## Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
         if x < 0:
            return False
        
         y = str(x)
         z = ""

         for i in range(len(y)-1, -1, -1):
            z += y[i]

         return int(z) == x
```

## Complexity Analysis

- **Time Complexity:** O(n²) for this exact implementation in the worst case, because repeated string concatenation can copy the growing string. The loop itself runs n times.
- **Space Complexity:** O(n) for the original string and reversed string.

## Key Learning

A number can be checked for palindrome by reversing its digits and comparing the reversed value with the original. This implementation performs the reversal using string indexing.
