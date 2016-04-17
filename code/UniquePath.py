# coding=utf8
# 题目: 给定一个m*n的方格, 机器人要从左上角位置到达右下角位置,有多少种不同的走法
# 思路: 动态规划, dp[i][j] = dp[i-1][j] + dp[i][j-1], 其中dp[i][j]表示到达i,j位置有多少种不同的走法

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

