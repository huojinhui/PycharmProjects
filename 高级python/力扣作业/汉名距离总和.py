from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]):
        he = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i] ^ nums[j]
                while a != 0:
                    a = a & (a - 1)
                    he += 1
        return he

s = Solution()
print(s.totalHammingDistance([4, 14, 2]))