# coding=utf8
class Solution(object):


    def lengthOfLIS(self,nums):
        """
        Complexity: O(nlogn)
        :param nums: List[int]
        :return: int
        """
        if not nums:
            return 0
        size = len(nums)
        max_len = 1
        dp = [0] * (size + 1)
        dp[1] = nums[0]
        for num in nums:
            low = 0
            high = max_len
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1
            dp[low] = num
            max_len = max(max_len,low)
        return max_len


    def lengthOfLIS2(self, nums):
        """
        Complexity: O(N^2)
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [1] * size

        for i in range(1,size):
            max_len = 0
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > max_len:
                    max_len = dp[j]
            dp[i] = max_len + 1
        return max(dp) if dp else 0

