# coding=utf8
# 主要有两个问题
# 1. 如何从数组中找到大小为t的最大子数组
# 2. 将两个子数组的最大子数组进行归并(两个子数组长度和为k)

class Solution(object):

    def max_array(self,nums, t):
        stack = []
        size = len(nums)
        for i in range(size):
            while stack and (size - i - 1) >= (t - len(stack)) and nums[i] > stack[-1]:
                stack.pop()
            if len(stack) < t:
                stack.append(nums[i])
        return stack

    def merge(self,nums1, nums2):
        size1 = len(nums1)
        size2 = len(nums2)
        index1, index2 = 0, 0
        ans = []
        while index1 < size1 and index2 < size2:
            if nums1[index1] > nums2[index2]:
                ans.append(nums1[index1]);
                index1 += 1
            else:
                ans.append(nums2[index2])
                index2 += 1
        while index1 < size1:
            ans.append(nums1[index1])
            index1 += 1
        while index2 < size2:
            ans.append(nums2[index2])
            index2 += 1
        return ans

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        size_1 = len(nums1)
        size_2 = len(nums2)
        ans = []
        for i in range(max(0,k - size_2),min(size_1,k)):
            subarray = self.merge(self.max_array(nums1,i), self.max_array(nums2, k - i))
            if subarray > ans:
                ans = subarray
        return ans