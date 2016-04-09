class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = nums[:]
        new_nums.insert(0, 1)
        new_nums.append(1)
        size = len(new_nums)

        dp = [[0] * (size) for _ in range(size)]
        for k in range(2, size):
            for l in range(0, size - k):
                r = l + k
                for m in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], dp[l][m] + new_nums[l] * new_nums[m] * new_nums[r] + dp[m][r])
        return dp[0][size-1]
