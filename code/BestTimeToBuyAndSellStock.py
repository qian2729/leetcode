# coding=utf8
# 题目: 给定一个数组,每个位置i的值表示第i天的股票价格,只允许进行一次买入和卖出,能够获得的最大收益
# 思路: 记录第i天之前的最低股票价格low, 计算price[i] - low是否为当前最大收益

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - low)
            low = min(low, prices[i])
        return max_profit