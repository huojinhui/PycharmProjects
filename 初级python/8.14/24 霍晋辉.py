# 0.写函数,返回一个扑克牌列表,里面有52项,每一项是一个元组
# 例如:
# 	[('红心','A'),('草花','A'),...,('方块','K'),('黑桃','K')]
#
# 第一个参数: ['红心','草花','方块','黑桃']
#
# 第二个参数: ['A','2','3','4',...,'K']
# def poker():
#     a = ['红心', '草花', '方块', '黑桃']
#     b = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#     # 做一个新列表接受元组
#     new = []
#     # 取出A到K
#     for i in b:
#         # 取出红心,,,,黑桃等
#         for j in a:
#            #列表内的元组
#            c = (j, i)
#            # 添加到新列表
#            new.append(c)
#     print(new)
#     return new
# poker()


# 笔试题目:
# 1.编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.
# 元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所
# 有数.
# def cacluate(*args):
#     # 求和的初始值
#     sum = 0
#     # 接受最后的结果
#     new = ()
#     # 求平均数
#     for i in args:
#         sum += i
#     average = sum / len(args)
#     new += (average,)
#     # 求出大于平均数的数
#     for i in args:
#         if i > average:
#             new += (i,)
#     print(new)


# 2.编写一个函数, 接收字符串参数, 返回一个元组,‘ehllo WROLD’
# 元组的第一个值为大写字母的个数, 第二个值为小写字母个数.
# def hello(a):
#     a = a.replace(' ', '')
#     countbig = 0
#     for i in a:
#         if i.islower():
#             countbig += 1
#     new = (countbig, len(a) - countbig)
#     print(new)
#     return new
# a = 'ehllo WROLD'
# hello(a)


# 3.编写函数, 接收一个列表(包含30个1~100之间的随机整形数)和一
# 个整形数k, 返回一个新列表.
# 函数需求:
# - 将列表下标k之前对应(不包含k)的元素逆序;
# - 将下标k及之后的元素逆序;
# [1,2,3,4,5] 2 [2,1,5,4,3]
# import random
# def fan(a, k):
#     # 接收列表
#     new_list = []
#     # 利用切片从后往前取达到翻转的要求
#     qian = a[k - 1::-1]
#     qian = sorted(qian, reverse=True)
#     new_list.extend(qian)
#     #同理
#     hou = a[len(a) - 1:k - 1:-1]
#     hou = sorted(hou, reverse=True)
#     new_list.extend(hou)
#     print(new_list)
#     return new_list
#
# # 下标随机生成
# k = random.randint(0, 29)
# # 生成一个1~100的列表
# b = [i for i in range(1, 101)]
# # 随机取出不重复的30个元素
# a = random.sample(b, 30)
# fan(a, k)

# 4.腾讯笔试题:
# 题目需求:
# 	f(n): 返回n里面的每一位数字的平方和
#     对于一个十进制的正整数， 定义f(n)为其各位数字的平方和，如:
#     f(13) = 1**2 + 3**2 = 10
#     f(207) = 2**2 + 0**2 + 7**2 = 53
#     下面给出三个正整数k，a, b,你需要计算有多少个正整数n满足a<=n<=b,
#     且k*f(n)=n
# 输入:
#     第一行包含3个正整数k，a, b, k>=1,  a,b<=10**18, a<=b;
# 输出：
#     输出对应的答案;
#
# 范例:
#     输入: 51 5000 10000
#     输出: 3 (这些数字n具体是哪些)

# 返回n里面的每一位数字的平方和
# def f(n):
#     # 转为字符串
#     n = str(n)
#     # 求和
#     sum = 0
#     for i in range(len(n)):
#         sum += int(n[i]) ** 2
#     return sum
#
# # 求n的个数
# k = int(input('请输入正整数k:'))
# a = int(input('请输入正整数a:'))
# b = int(input('请输入正整数b:'))
# for i in range(a, b + 1):
#     if i == k * f(i):
#         print(i, end=' ')