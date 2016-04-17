# coding=utf8
# 题目: 给定整数n,给出最少可以用几个完全平方数的和得到n, 完全平方数指由整数的平方组成的数,比如1,4,9
# 思路: 借鉴数论中的四平方和定理(任意一个正整数均可以表示为4个以内完全平方数的和),这个定理告诉我们,返回结果只可能为1,2,3或4
# 另外两个可以简化搜索空间的方法: 如果一个数含有因子4,那么,把这个数除以4,并不影响结果(4*任意正整数都是完全平方数)
# 如果一个数除以8余7的话,那么肯定由4个完全平方数组成
# 剩下的结果因为缩小了搜索空间,直接枚举就可以了
import math
class Solution(object):

    def numSquares(self,n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 0
        while i * i <= n:
            b = int(math.sqrt(n - i * i))
            if (i * i + b * b) == n:
                return int(not not i) + int(not not b)
            i += 1
        return 3

    # Complexity: O(n * sqrt(n))
    # Time limited
    def numSquares_fail(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n + 1)
        i = 1
        while i * i <= n:
            dp[i*i] = 1
            i += 1
        for i in range(2, n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j*j] = min(dp[i+j*j],dp[i] + 1)
                j += 1

        return dp[n]
print Solution().numSquares(6)