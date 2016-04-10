# coding=utf8
# 给定一个数组,计算和最大的子数组,子数组至少要有一个元素
# 思路: 利用一个变量存储到当前位置之前的最大子数组的和, cur_max = max(cur_max + nums[i], nums[i])如果cur_max < 0 则以当前元素作为
# 最大子数组的第一个元素

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_ans = cur_max = nums[0]
        for i in range(1,len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            max_ans = max(cur_max, max_ans)
        return max_ans
