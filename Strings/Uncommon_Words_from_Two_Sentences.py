"""
LeetCode 884 - Uncommon Words from Two Sentences
Problem: https://leetcode.com/problems/uncommon-words-from-two-sentences/

Approach: Word Frequency Dictionary

How I Solved It:
1. Split both sentences into words and combine the two lists.
2. Create a dictionary to count how many times each word appears.
3. Use a list comprehension to select words whose frequency is exactly 1.
4. Return those words.

Why it works:
A word is uncommon when it appears exactly once across both sentences.
The frequency dictionary lets us check that condition for every word.

Time Complexity: O(n + m), where n and m are the total numbers
of characters in the two sentences (including splitting and counting).
Space Complexity: O(n + m) for the word lists, frequency dictionary,
and result in the worst case.
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        new_list = s1.split(" ") + s2.split(" ")
        x=dict()
        for i in new_list:
            if i in x:
               x[i]=x[i]+1
            else:
               x[i]=1
        ans=[i for i in new_list if x[i]==1]          
        return ans
