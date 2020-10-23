# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的
# target，如果目标值存在返回下标，否则返回 -1。
from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            if target == nums[head]:
                return head
            elif target == nums[tail]:
                return tail
            else:
                mid = int((head + tail) / 2)
                if target < nums[mid]:
                    tail = mid - 1
                elif target > nums[mid]:
                    head = mid + 1
                else:
                    return mid
        return -1



a = Solution()
print(a.search([-1, 0, 3, 5, 9, 12], -1))

