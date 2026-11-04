# 6. Zigzag Conversion

**LeetCode:** [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)  
**Topic:** Strings  
**Difficulty:** Medium

## My Approach

I created one string bucket for each row and used an index and direction variable to simulate the zigzag traversal.

1. If there is only one row, or the number of rows is at least the string length, return the original string.
2. Append each character to the current row.
3. Change direction at the top and bottom rows.
4. Join all row strings to get the final result.

## Solution

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)
```

## Complexity Analysis

Let `n` be the length of the input string.

- **Time Complexity:** O(n) — each character is visited once, and the final join processes all characters.
- **Space Complexity:** O(n) — the row strings collectively store all input characters.

## Key Learning

A direction variable makes it easy to simulate movement down and up through the rows without constructing a two-dimensional zigzag matrix.
