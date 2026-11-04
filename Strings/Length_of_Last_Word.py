"""
LeetCode 58 - Length of Last Word
Problem: https://leetcode.com/problems/length-of-last-word/

Approach: Split the String into Words

How I Solved It:
1. Use split() to separate the string into words.
   With no separator supplied, split() also handles leading,
   trailing, and repeated whitespace.
2. Select the last word using words[-1].
3. Return the length of that word.

Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(n) for the list of words created by split().
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        return(len(words[-1]))
