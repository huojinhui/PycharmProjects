# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        mincount = float("inf")
        cursum = 0

        for right in range(len(nums)):
            left = 0
            cursum += nums[right]

            while cursum >= s:
                mincount = min(mincount, right - left + 1)
                cursum = cursum - nums[left]
                left += 1
            return mincount if mincount != float("inf") else 0


    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        left = 0
        mincount = float('inf')
        cursum = 0

        for right in range(len(nums)):
            cursum += nums[right]

            while cursum >= s:
                mincount = min(mincount, right - left + 1)
                cursum = cursum - nums[left]
                left += 1

        return mincount if mincount != float('inf') else 0


