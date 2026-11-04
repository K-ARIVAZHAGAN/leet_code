# 520. Detect Capital

**LeetCode:** [Detect Capital](https://leetcode.com/problems/detect-capital/)  
**Topic:** Strings  
**Difficulty:** Easy

## My Approach

I use Python's built-in string methods to check the three valid capitalization patterns:

1. The entire word is uppercase.
2. The entire word is lowercase.
3. Only the first letter is uppercase and the remaining letters are lowercase.

If any one of these conditions is true, return `True`; otherwise, return `False`.

## Solution

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper():
            return True
        elif word==word.lower():
            return True
        elif word==word.capitalize():
            return True
        return False
```

## Complexity Analysis

Let `n` be the length of the word.

- **Time Complexity:** O(n) — the string comparison methods examine the characters in the word.
- **Space Complexity:** O(n) — Python's case-conversion methods may create new strings.

## Key Learning

Python's `upper()`, `lower()`, and `capitalize()` methods make it straightforward to validate the three allowed capitalization patterns.
