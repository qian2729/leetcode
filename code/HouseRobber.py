# coding=utf8
# 题目: 给定非负整数组成的列表,每个元素表示一个家庭可窃取的金额,不能窃取相邻两个家庭的钱财,问最多能够窃取多少钱
# 思路: 动态规划, dp[i] = max(dp[i-1], dp[i-2] + nums[i]), dp[i] 表示窃取到第i家最多窃取的金额

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        dp = [0] * (size + 1)
        dp[1] = nums[0]
        for i in range(2,size + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i - 1])
        return dp[-1]
