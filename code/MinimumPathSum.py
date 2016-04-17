# coding=utf8
# 题目: 一个m*n的方格,每个方格有一个非负整数,求从方格左上角到达右下角的最小路径和,只能向右和向下走
# 思路: 动态规划, dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j], dp[i][j] 为到达i,j位置的最短路径和

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]