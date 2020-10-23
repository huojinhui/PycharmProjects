from typing import List
# 删除重复元素


class solution:
    def removeRepeat(self, nums: List):
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1

    def remove_two_repeat(self, nums: List):
        fast = 1
        slow = 0
        count = 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                count += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
                    fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1

    # 原理是先将不为0的往前移,然后将slow后面的变为0
    def remove_zero(self, nums):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
