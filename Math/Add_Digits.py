# 258. Add Digits

**LeetCode:** [Add Digits](https://leetcode.com/problems/add-digits/)  
**Topic:** Math  
**Difficulty:** Easy

## My Approach

I used the digital-root formula instead of repeatedly adding the digits.

- If the number is `0`, return `0`.
- Otherwise, return `1 + (num - 1) % 9`.

This uses the mathematical property that the digital root of a positive integer can be calculated using modulo 9.

## Solution

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
```

## Complexity Analysis

- **Time Complexity:** O(1) — a fixed number of arithmetic operations.
- **Space Complexity:** O(1) — no additional data structure is used.

## Key Learning

The digital root can be calculated directly using modulo 9, without repeatedly extracting and adding digits.
