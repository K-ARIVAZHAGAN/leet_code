# 66. Plus One

**LeetCode:** [Plus One](https://leetcode.com/problems/plus-one/)  
**Topic:** Arrays  
**Difficulty:** Easy

## My Approach

I converted the digit array into a single integer by processing each digit:

1. Multiply the current number by 10 and add the next digit.
2. Add one to the resulting number.
3. Convert the updated number to a string, then convert each character back into an integer and append it to a new list.

## Solution

```python
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0

        for i in digits:
            n = n * 10 + i

        n += 1

        a = []
        for i in str(n):
            a.append(int(i))

        return a
```

## Complexity Analysis

- **Time Complexity:** O(n) — building the integer and converting the result back to a list both take linear time in the number of digits.
- **Space Complexity:** O(n) — the output list and string representation require space proportional to the number of digits.

## Key Learning

An array of digits can be converted into an integer by repeatedly multiplying the current value by 10 and adding the next digit.
