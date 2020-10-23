# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#  
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        different = []
        he = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    sum = (nums[i] + nums[j] + nums[k])
                    he.append(sum)
                    different.append(abs(target - sum))
        small = min(different)
        a = different.index(small)
        return he[a]

    def threeSumClosest1(self, nums: List[int], target: int):
        res = []
        cha = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                he = nums[i] + nums[left] + nums[right]
                res.append(he)
                cha.append(abs(target - he))
                left += 1
        small = min(cha)
        print(res)
        return res[cha.index(small)]







a = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(a.threeSumClosest1(nums, target))
