"""
LeetCode 125 - Valid Palindrome
Problem: https://leetcode.com/problems/valid-palindrome/

Approach: Clean the String and Compare It with Its Reverse

How I Solved It:
1. If the string has zero or one character, return True.
2. Convert the string to lowercase so comparison is case-insensitive.
3. Build a new string containing only alphanumeric characters.
4. Reverse the cleaned string using slicing.
5. Compare the cleaned string with its reverse.
6. Return the comparison result.

Key Learning:
str.isalnum() keeps letters and numbers while filtering out spaces
and punctuation. The [::-1] slice creates the reversed string.

Time Complexity: O(n)
Space Complexity: O(n) for the cleaned and reversed strings.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        s=s.lower()
        new_s=''
        for i in s:
            if i.isalnum():
                new_s +=i
        return  new_s == new_s[::-1]
