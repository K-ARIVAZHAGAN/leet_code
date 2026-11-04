# 1. Two Sum

**LeetCode:** [Two Sum](https://leetcode.com/problems/two-sum/)  
**Topic:** Arrays  
**Difficulty:** Easy

## My Approach

I used two nested loops to check every possible pair of elements.

1. The outer loop selects the first element using index `i`.
2. The inner loop starts from `i + 1`, so the same element is never used twice.
3. If the sum of the two elements equals `target`, return their indices.

## Solution

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

## Complexity Analysis

- **Time Complexity:** O(n²) — for each element, the inner loop may check the remaining elements.
- **Space Complexity:** O(1) — only a fixed amount of extra space is used.

## Key Learning

Starting the inner loop at `i + 1` avoids checking the same pair twice and prevents using the same array element two times.
