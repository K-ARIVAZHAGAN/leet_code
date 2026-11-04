"""
LeetCode 290 - Word Pattern
Problem: https://leetcode.com/problems/word-pattern/

Approach: Hash Map + Set (One-to-One Mapping)

How I Solved It:
1. Split the sentence into a list of words.
2. If the number of words differs from the pattern length, return False.
3. Use a dictionary to map each pattern character to a word.
4. Use a set to track words that are already mapped.
5. For each character-word pair:
   - If the character already has a mapping, check that it maps
     to the current word.
   - Otherwise, reject the pair if the word is already used.
   - If it is unused, create the mapping and record the word.
6. If every pair matches, return True.

Key Learning:
The dictionary checks character-to-word consistency, while the set
prevents two different characters from mapping to the same word.

Time Complexity: O(n) average, where n is the number of words.
Space Complexity: O(n) for the words, mapping, and set.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        mapping = {}
        used = set()

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in mapping:
                if mapping[char] != word:
                    return False
            else:
                if word in used:
                    return False

                mapping[char] = word
                used.add(word)

        return True
