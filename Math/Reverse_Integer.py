# 7. Reverse Integer

**LeetCode:** [Reverse Integer](https://leetcode.com/problems/reverse-integer/)  
**Topic:** Math  
**Difficulty:** Medium

## My Approach

I separated the sign from the number, reversed the absolute value as a string, converted it back to an integer, and restored the original sign.

I then used `bit_length()` as an overflow check.

## Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = 1
        else:
            sign = -1
        a = abs(x)
        b = str(a)[::-1]
        c = int(b)
        x = c * sign
        if x.bit_length() < 32:
            return x
        else:
            return 0
```

## Complexity Analysis

- **Time Complexity:** O(n) — converting, reversing, and converting back take time proportional to the number of digits.
- **Space Complexity:** O(n) — the string representation and reversed string use space proportional to the number of digits.

## Important Boundary Note

The submitted `bit_length() < 32` check does not exactly match LeetCode's signed 32-bit range. In particular, the valid value `-2147483648` has a bit length of 32 and would be returned as `0`. The exact range check is `-(2**31) <= x <= (2**31 - 1)`. The original submitted code is preserved above.

## Key Learning

Separate the sign before reversing the digits, then validate the result against the required integer range.
