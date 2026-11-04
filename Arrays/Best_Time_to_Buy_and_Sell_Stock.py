"""
LeetCode 121 - Best Time to Buy and Sell Stock
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach: Track the Minimum Price and Maximum Profit

How I Solved It:
1. Start by treating the first price as the minimum price seen so far.
2. Initialize maximum profit to 0.
3. Traverse the prices:
   - Calculate the profit from buying at the minimum price seen so far
     and selling at the current price.
   - Update maximum profit if this profit is higher.
   - Update the minimum price if the current price is lower.
4. Return the maximum profit.

Why the order matters:
Calculate profit before updating the minimum price. This ensures
the buy price comes from an earlier day than the sell price.

Time Complexity: O(n)
Space Complexity: O(1)

Note: The LeetCode constraints guarantee that prices is non-empty.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            profit = prices[i] - min_price

            if profit > max_profit:
                max_profit = profit

            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit
