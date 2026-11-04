# 4. Median of Two Sorted Arrays

**LeetCode:** [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)  
**Topic:** Binary Search / Arrays  
**Difficulty:** Hard

## My Approach

I use two pointers, one for each sorted array, to simulate merging them in sorted order without creating a merged array.

- `med1` stores the most recently selected value.
- `med2` stores the previously selected value.
- At each step, I select the smaller available element from the two arrays and advance its pointer.
- I stop after reaching the middle position.

For an even total length, the median is the average of the two middle values. For an odd total length, it is the most recently selected middle value.

## Solution

```python
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        med1 = med2 = i = j = 0
        n = len(A) + len(B)
        
        while (i + j) <= n / 2:
            if i < len(A) and j < len(B):
                med2 = med1
                if A[i] < B[j]:
                    med1 = A[i]
                    i += 1
                else:
                    med1 = B[j]
                    j += 1
            elif i < len(A):
                med2 = med1
                med1 = A[i]
                i += 1
            elif j < len(B):
                med2 = med1
                med1 = B[j]
                j += 1

        if n % 2 == 0:
            return (med1 + med2) / 2.0
        else:
            return med1
```

## Complexity Analysis

Let `m` and `n` be the lengths of the two arrays.

- **Time Complexity:** O(m + n) — at most about half of the combined elements are traversed.
- **Space Complexity:** O(1) — only pointers and two median values are stored.

## Key Learning

Two pointers can find the middle values of two sorted arrays without allocating a separate merged array.

## Note

This is a linear merge-style approach, not the optimal O(log(min(m, n))) binary-partition solution expected by the problem's advanced follow-up.
