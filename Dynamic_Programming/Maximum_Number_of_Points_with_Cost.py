# 1937. Maximum Number of Points with Cost

**LeetCode:** [Maximum Number of Points with Cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/)  
**Topic:** Dynamic Programming  
**Difficulty:** Medium

## My Approach

I used dynamic programming with two directional passes for each row.

- `dp[j]` stores the best score when the previous row's selected column is `j`.
- The left-to-right pass tracks the best previous score while accounting for the movement cost.
- The right-to-left pass does the same from the opposite direction.
- For each column, I take the better of the two directional values and add the current row's points.

After processing all rows, the maximum value in `dp` is the answer.

## Solution

```python
class Solution:
  def maxPoints(self, points: list[list[int]]) -> int:
    n = len(points[0])
    # dp[j] := the maximum number of points you can have if points[i][j] is the
    # most recent cell you picked
    dp = [0] * n

    for row in points:
      leftToRight = [0] * n
      runningMax = 0
      for j in range(n):
        runningMax = max(runningMax - 1, dp[j])
        leftToRight[j] = runningMax

      rightToLeft = [0] * n
      runningMax = 0
      for j in range(n - 1, - 1, -1):
        runningMax = max(runningMax - 1, dp[j])
        rightToLeft[j] = runningMax

      for j in range(n):
        dp[j] = max(leftToRight[j], rightToLeft[j]) + row[j]

    return max(dp)
```

## Complexity Analysis

Let `m` be the number of rows and `n` the number of columns.

- **Time Complexity:** O(m × n) — each row is processed with a constant number of linear passes.
- **Space Complexity:** O(n) — the DP array and two directional arrays are proportional to the number of columns.

## Key Learning

Two directional running-maximum passes optimize the row transition, avoiding a quadratic scan over every pair of columns.
