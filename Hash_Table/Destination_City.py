"""
LeetCode 1436 - Destination City
Problem: https://leetcode.com/problems/destination-city/

Approach: Set Lookup

How I Solved It:
1. Build a set containing every starting city.
2. Traverse each path (start, destination).
3. The destination city that does not appear in the set of starting
   cities is the final destination.
4. Return that city.

Key Learning:
A set provides efficient membership checks, making it easy to find
the city that never appears as a departure point.

Time Complexity: O(n) average, where n is the number of paths.
Space Complexity: O(n) for the set.
"""

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starts = {path[0] for path in paths}

        for start, destination in paths:
            if destination not in starts:
                return destination
