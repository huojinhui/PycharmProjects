# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000
class Solution:
    def longest_palindrome(self, s: str) -> str:
        # 输入字符串长度
        length = len(s)
        # 如果只有哦一个字符直接返回
        if length < 2:
            return s
        # 假设最大长度为1, 最长的回文字符串为第一个字符
        maxlen = 1
        res = s[0]
        for i in range(length - 1):
            # 以i为回文子串中点进行中心扩展
            odd = self.center_spread(s, i, i)
            # 以i 和i + 1为回文子串中点进行回文扩展
            event = self.center_spread(s, i, i + 1)
            # 判断哪个更长
            maxstr = odd if len(odd) > len(event) else event
            # 将最长的和maxlen比较然后输出最长的
            if len(maxstr) > maxlen:
                maxlen = len(maxstr)
                res = maxstr
        return res

    def center_spread(self, strs: str, left, right) -> str:
        length = len(strs)
        i = left
        j = right
        # 对中心元素进行扩展,对比左右,如果相等则继续否则终止
        while i >= 0 and j < length:
            if strs[i] == strs[j]:
                i -= 1
                j += 1
            else:
                break
        return strs[i + 1: j]


a = Solution()
b = "acvca"
print(a.longest_palindrome(b))
