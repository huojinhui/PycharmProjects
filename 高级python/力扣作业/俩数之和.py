# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

    def twoSum1(self, nums: List[int], target: int):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

    # 对撞指针
    def twoSum3(self, nums: List[int], target: int):
        head = 0
        tail = len(nums) - 1
        while head < tail:
            if target == nums[head] + nums[tail]:
                print(nums[head], nums[tail])
                head += 1
                tail -= 1
            else:
                if nums[head] + nums[tail] < target:
                    head += 1
                else:
                    tail -= 1

    def twoSum4(self, nums: List[int], target: int):
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [i, dic[temp]]
            else:
                dic[nums[i]] = i


