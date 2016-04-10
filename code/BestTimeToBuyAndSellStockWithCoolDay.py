# coding=utf8
# 给定一个数组,其中的每个位置i表示第i天的股票价格,可以进行任意多次交易,但是必须先卖掉之前的股票才能再买,同时要求
# 卖掉股票之后的第二天不能再买股票(称为冷冻期), 问最多能获得多少收益.
# 思路: 此题需要有两个数组来存储最大收益,
# sell: 存储第i天之前最后一个操作为卖,能够得到的最大收益
# buy: 存储第i天之前最后一个操作为买,能够得到的最大收益
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        num = len(prices)
        sell = [0] * num
        buy = [0] * num
        buy[0] = -prices[0]
        for i in range(1,num):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        return sell[-1]
