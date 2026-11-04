"""
LeetCode 392 - Is Subsequence
Problem: https://leetcode.com/problems/is-subsequence/

Approach: Two Pointers (Single Pass)

How I Solved It:
1. If s is empty, return True because an empty string is a subsequence
   of every string.
2. If s is longer than t, return False.
3. Use char to track the next character of s that must be matched.
4. Traverse t from left to right.
5. Whenever t[j] matches s[char], move char forward.
6. Stop early once all characters in s have been matched.
7. Return whether char reached len(s).

Other Approaches You Considered:
- A while-loop version of the same two-pointer idea.
- A nested-loop approach that searches for each character in order.

Time Complexity: O(len(t))
Space Complexity: O(1), excluding input strings.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0:
            return True
        elif len(s) > len(t):
            return False
        char = 0
        for j in range(len(t)):
            if char == len(s):
               break
            if s[char] == t[j]:
                char += 1
        return char == len(s)
        '''==================================
        method 2.Using while O(t)
        =====================================
         if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        char = 0
        j = 0

        while j < len(t) and char < len(s):
            if s[char] == t[j]:
                char += 1
            j += 1

        return char == len(s)
    ===========================================   
        method 3.Using Nested Loop. O(s * t)
    ===========================================
        if len(s) > len(t):
            return False
        match = 0
        for i in range(len(s)):
            for j in range(match,len(t)):
                if s[i] == t[j]:
                    match = j + 1
                    break
            else:
                return False
        return True
    '''
