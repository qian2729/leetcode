# coding=utf8
# 有一个n级台阶,每次可以上一个或两个台阶,问要爬过n级台阶有多少种不同的走法
# 斐波那契数列的变种. 第一步可以走1个台阶剩余n-1个台阶或走2个台阶,剩余n-2个台阶,有f(n-1) + f(n-2)种不同的走法

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
