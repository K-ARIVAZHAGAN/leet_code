# 1394. Find Lucky Integer in an Array

**LeetCode:** [Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-in-an-array/)  
**Topic:** Hash Table  
**Difficulty:** Easy

## My Approach

I used a dictionary to count the frequency of each number.

1. Iterate through the array and build a frequency dictionary.
2. Iterate through the dictionary.
3. If a number is equal to its frequency, it is a lucky integer.
4. Track the largest lucky integer found. If none exists, return `-1`.

## Solution

```python
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq={}
        freql=-1
        for i in arr:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        for i in freq:
            if i == freq[i] and freql < i:
                  freql=i
        return freql
```

## Complexity Analysis

Let `n` be the length of the input array and `u` the number of distinct values.

- **Time Complexity:** O(n + u), which is O(n) — build the frequency dictionary in one pass, then inspect each distinct value.
- **Space Complexity:** O(u) — the dictionary stores one entry per distinct value.

## Key Learning

A frequency dictionary makes it easy to identify values whose occurrence count matches the value itself. Tracking the maximum ensures the largest lucky integer is returned.
