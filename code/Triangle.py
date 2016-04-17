# coding=utf8
# 题目: 给定一个三角形二维数组(第一行有1个元素,以后每一行递增一个元素),求从第一行到最后一行路径的最短路径和
# 思路:

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        MAX_INT = (1 << 32) - 1
        dp = [triangle[0][0]]
        for i in range(1, len(triangle)):
            tmp = [MAX_INT] * (i + 1)
            for j in range(i + 1):
                tmp[j] = min(dp[j], dp[j+1]) + triangle[i][j] if j
                tmp[j] = min(dp[j],dp[j+1])
                # tmp[j + 1] = min()
    