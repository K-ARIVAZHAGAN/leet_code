# 624. Maximum Distance in Arrays

**LeetCode:** [Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/)  
**Topic:** Arrays  
**Difficulty:** Medium

## My Approach

I track the smallest first element and largest last element seen in the previous arrays.

For each current array:
1. Compare its last element with the smallest value from previous arrays.
2. Compare the largest value from previous arrays with its first element.
3. Update the answer with the largest valid distance.
4. Update the minimum and maximum values for the next iteration.

Updating the answer before updating `mn` and `mx` ensures the two values come from different arrays.

## Solution

```python
class Solution:
  def maxDistance(self, arrays: list[list[int]]) -> int:
    ans = 0
    mn = 10000
    mx = -10000

    for A in arrays:
      ans = max(ans, A[-1] - mn, mx - A[0])
      mn = min(mn, A[0])
      mx = max(mx, A[-1])

    return ans
```

## Complexity Analysis

Let `k` be the number of arrays.

- **Time Complexity:** O(k) — each array is processed once.
- **Space Complexity:** O(1) — only a fixed number of variables are used.

## Key Learning

Maintaining the global minimum and maximum from previously processed arrays allows the maximum distance to be found in one pass.
