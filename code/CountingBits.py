# coding=utf8
# 给定计算0~N之间每个数的二进制表示中1的个数
# 思路: 所有2的次幂的数的二进制表示中都只有1个1,其他数的二进制表示中1的数量为与其二进制中最高位的2次幂的差所对应的二进制表示中1的数量+1
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [num]
        dp = [0] * (num + 1)
        dp[1] = 1
        last_num = 1
        next_num = 2
        for i in range(2,num + 1):
            if i == next_num:
                dp[i] = 1
                last_num = i
                next_num = i * 2
            else:
                dp[i] = dp[i - last_num] + 1
        return dp
