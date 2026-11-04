"""
LeetCode 292 - Nim Game
Problem: https://leetcode.com/problems/nim-game/

Approach: Mathematical Observation (Modulo)

How I Solved It:
1. Return whether n % 4 is not equal to 0.
2. If the number of stones is a multiple of 4, the first player
   cannot force a win when both players play optimally.
3. Otherwise, the first player can take enough stones (1, 2, or 3)
   to leave a multiple of 4 for the opponent.

Key Learning:
Instead of simulating every possible move, recognizing the repeating
pattern of losing positions gives a constant-time solution.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0
