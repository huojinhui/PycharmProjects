# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。


class Solution:
    def hammingDistance(self, x: int, y: int):
        a = x ^ y
        count = 0
        while a != 0:
            a = a & (a - 1)
            count += 1
        return count


s = Solution()
print(s.hammingDistance(4, 8))
print(bin(8))
