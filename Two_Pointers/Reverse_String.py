"""
LeetCode 344 - Reverse String
Problem: https://leetcode.com/problems/reverse-string/

Approach: Copy, Clear, and Insert at the Beginning

How I Solved It:
1. Make a copy of the original list.
2. Clear the input list.
3. Traverse the copied characters.
4. Insert each character at index 0 of the input list.
5. The original list is now reversed in-place.

Important Complexity Note:
Inserting at index 0 shifts the existing elements each time.
Therefore, this implementation takes O(n^2) time.
The copy also requires O(n) extra space.

The problem asks for an in-place modification; this solution modifies
the original list, but uses an additional copy. A two-pointer swap
approach can achieve O(n) time and O(1) auxiliary space.
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x=s.copy()
        s.clear()
        for i in x:
            s.insert(0,i)
