"""
LeetCode 242 - Valid Anagram
Problem: https://leetcode.com/problems/valid-anagram/

Approach: Sorting and Comparing

How I Solved It:
1. If the strings have different lengths, return False.
2. Convert both strings into lists of characters.
3. Sort both lists.
4. Compare corresponding characters.
5. If any character differs, return False.
6. If every character matches, return True.

Other Approaches You Considered:
- A frequency dictionary that increments counts for s and decrements
  them for t. This can run in O(n) average time.
- Repeated str.count() checks, which can take O(n^2) time.

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(n) for the character lists and sorting.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' #method 3  (O(n))

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True

        ===========================================
        method -2 (O(n^2))
        if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True 
        =======================================
        '''
        #method-1  (O(n log n))
        if len(s) != len(t):
            return False
        x=[i for i in s]
        y=[i for i in t]
        x.sort()
        y.sort()
        for i in range(len(s)):
            if x[i] != y[i]:
               return False
        return True
