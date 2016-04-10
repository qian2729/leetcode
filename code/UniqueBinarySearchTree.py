# coding=utf8
# 给定1~N组成的数,能够组成多少种不同的二叉搜索数
# 思路: 将每个数i作为根节点,所有小于i的数组成二叉搜索数的数量*大于i的数组成的二叉搜索数数量之和

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j-1] * dp[i - j]
        return dp[n]