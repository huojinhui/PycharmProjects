# 给定一个包含非负整数的数组,统计其中可以组成三角形三条边的三元组个数
from typing import List


class Solution:
    def triangle_count(self, nums: List):
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 0, -1):  # 固定最右边的数为最大边
            left = 0
            right = i - 1
            while left < right:
                he = nums[left] + nums[right]
                if he > nums[i]:
                    count += (right - left)  # 如果he大于第三边则后面的都大于第三边
                    right -= 1
                else:
                    left += 1
        return count


a = Solution()
print(a.triangle_count([2, 2, 3, 4]))
