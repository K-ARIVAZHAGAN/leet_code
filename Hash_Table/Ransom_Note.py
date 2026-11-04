"""
LeetCode 383 - Ransom Note
Problem: https://leetcode.com/problems/ransom-note/

Approach: Character Frequency Counting with str.count()

How I Solved It:
1. Iterate through each character in ransomNote.
2. Compare how many times that character occurs in ransomNote
   with how many times it occurs in magazine.
3. If ransomNote needs more copies than magazine contains,
   return False.
4. If no character exceeds the available count, return True.

Key Learning:
A character can only be used as many times as it appears in magazine.

Complexity Note:
str.count() scans the string each time it is called. Repeating it
inside the loop makes this slower than building a frequency dictionary.
A simple upper bound is O(r * (r + m)), where r and m are the
lengths of ransomNote and magazine.
Space Complexity: O(1) auxiliary space for this implementation.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
