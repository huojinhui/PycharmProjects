from typing import List


class Solution:
    def sortcolors1(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            flag = 1
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = 2
            if flag == 1:
                break
            print(f"第{i + 1}次排序", nums)
        return nums

    def sortcolors2(self, nums: List[int]) -> None:
        # a, b是色块, c是指针
        a = c = 0
        b = len(nums) - 1
        while c <= b:
            if nums[c] == 0:
                nums[a], nums[c] = nums[c], nums[a]
                c += 1
                a += 1
            elif nums[c] == 2:
                nums[c], nums[b] = nums[b], nums[c]
                b -= 1
            else:
                c += 1
        return nums


a = Solution()
print(a.sortcolors2([1, 1, 2, 0]))
