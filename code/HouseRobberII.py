# coding=utf8
# 题目: 给定一个非负整数组成的列表,每个元素表示一个住户可以窃取的金额,不能同时窃取相邻两家,第一家和最后一家相邻,求最多能够窃取多少钱
# 思路: 与HouseRobber不同的只有第一个元素和最后一个元素是相邻的,所以分别计算0~n-2和1~n-1两种情况,求最大值

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.linear_rob(nums[1:]),self.linear_rob(nums[:-1]))

    def linear_rob(self,nums):
        if not nums:
            return 0
        size = len(nums)
        dp = [0] * (size + 1)
        dp[1] = nums[0]
        for i in range(2,size + 1):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i-1])
        return dp[size]