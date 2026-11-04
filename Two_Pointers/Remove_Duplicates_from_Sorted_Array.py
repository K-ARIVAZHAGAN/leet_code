# 26. Remove Duplicates from Sorted Array

**LeetCode:** [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)  
**Topic:** Two Pointers  
**Difficulty:** Easy

## My Approach

I used a slow pointer `k` to track the position where the next unique element should be placed.

1. Start with `k = 0`.
2. Iterate through the array.
3. If this is the first element, or the current value differs from the last unique value at `nums[k - 1]`, copy it to `nums[k]`.
4. Increment `k) whenever a unique value is found.
5. Return `k`, the number of unique elements.

## Solution

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k == 0 or nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k
```

## Complexity Analysis

- **Time Complexity:** O(n) — each element is visited once.
- **Space Complexity:** O(1) — the array is modified in place.

## Key Learning

A slow pointer can track the position of the next unique element while a fast pointer scans the array.
