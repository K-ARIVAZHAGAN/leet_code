"""
LeetCode 1768 - Merge Strings Alternately
Problem: https://leetcode.com/problems/merge-strings-alternately/

Approach: Two Index Pointers

How I Solved It:
1. Initialize an empty result string and two indexes, one for each word.
2. Continue while the result length is smaller than the combined
   lengths of both input strings.
3. If the first word still has characters, append its next character
   and move its index forward.
4. If the second word still has characters, append its next character
   and move its index forward.
5. Return the merged string.

Key Learning:
The separate bounds checks allow the loop to handle strings of
different lengths without accessing an invalid index.

Time Complexity: O((m + n)^2) for this exact implementation because
repeated string concatenation creates new strings.
Space Complexity: O(m + n) for the resulting string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        x=0
        i=0
        while (len(word1)+len(word2))>len(res):
           if x != len(word1):
                res = res+word1[x]
                x+=1
           if i < len(word2): 
                res=res+word2[i]
                i+=1
        return res
