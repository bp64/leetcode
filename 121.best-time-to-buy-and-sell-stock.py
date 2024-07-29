#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (53.94%)
# Likes:    31000
# Dislikes: 1164
# Total Accepted:    5M
# Total Submissions: 9.2M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 1
        # O(n), 80%
        # iterate through array
        # track the lowest price seen and profit
        # if selling on the current element makes more potential profit than what we've seen update profit

        min_price_seen = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            potential_profit = current_price - min_price_seen

            if current_price < min_price_seen:
                min_price_seen = current_price
            if potential_profit > profit:
                profit = potential_profit

        return profit


# @lc code=end
