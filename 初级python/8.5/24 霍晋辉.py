# 1. 计算从1到1000以内所有能被3或者17整除的数的和并输出
# i = 1
# sum = 0
# while i<= 1000:
#     if i % 3 == 0 or i % 17 == 0:
#         sum += i
#     i += 1
# print(sum)


# 2. 求1到10的阶乘 (格式为 5的阶乘为: 120 )
# 	5: 5 * 4 * 3 * 2 * 1
# 	4: 4 * 3 * 2 * 1
# 	3: 3 * 2 * 1
# 	2: 2 * 1
# 	1: 1
# 	结果:
# 	5的阶乘为: 120
# 	4的阶乘为: 120
# 	3的阶乘为: 120
# 	2的阶乘为: 120
# 	1的阶乘为: 120
#
# i = 1
# ji = 1
# while i <= 10:
#     ji *= i
#     print('%s的阶乘为:%s' % (i, ji))
#     print()
#     i += 1


# 3. 求一到十阶乘之和。(1: 1 2: 2  3: 6  4: 24 5: 120)
# i = 1
# ji = 1
# he = 0
# while i <= 10:
#     ji = ji * i
#     he += ji
#     i += 1
# print(he)

# 4. 功能：用户登录(三次机会尝试)
# 用户名密码：
# name = "aaa"
# password = "123"
# 让用户输入，如果输入正确，显示登录成功， 失败，显示还有几次机会， 超过三次失败，显示失去登录机会，明天再来。退出程序。

# i = 3
# while i >= 1:
#     name = input('请输入用户名:')
#     password = input('请输入密码:')
#     if name == 'aaa' and password == '123':
#         print('登陆成功')
#         exit()
#     else:
#         b = i - 1
#         if b != 0:
#             print('登陆失败,还有%s次机会,请珍重.'%(b))
#         else:
#             break
#     i -= 1
# print('失去登陆机会,明天再来.')



# 5. 打印出所有的“水仙花数”。
# 所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。
# i = 100
# while i < 1000:
#     bai = i // 100
#     ge = i % 10
#     shi = i // 10 % 10
#     he = bai ** 3 + shi ** 3 + ge ** 3
#     if he == i:
#         print(he)
#     i += 1
# print(sum)

 
# 6.五位数中，对称的数称为回文数，打印所有的回文数并计算个数。如:12321
# i = 10000
# cunt = 0
# while i < 100000:
#     one   = i // 10000
#     two   = int(i // 1000) % 10
#     three = int(i // 100) % 10
#     four  = int(i // 10) % 10
#     five  = i % 10
#     if one == five and two == four :
#         print(i)
#         cunt += 1
#         print(cunt)
#     i += 1
# print(cunt)

#
# 7.公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？
# i = 1
# he = 1
# while i <= 6:
#     he = (he + 1) * 2
#     i += 1
# print(he)


# 关于嵌套循环的练习:
#
# 1.输出9行内容，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789
#
# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, end='')
#         j += 1
#     print()
#     i += 1


# 2.打印菱形
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# spaceCount = 3
# count = 1
# while spaceCount >= 0:
#     print(spaceCount * ' ', end='')
#     print(count * '*')
#     spaceCount -= 1
#     count += 2
# spaceCount = 1
# count = 5
# while spaceCount <= 3:
#     print(spaceCount * ' ', end='')
#     print(count * '*')
#     spaceCount += 1
#     count -= 2
# 3.打印九九乘法表
# 1 * 1 = 1
# 1 * 2 = 2	2 * 2 = 4
# 1 * 3 = 3	2 * 3 = 6	3 * 3 = 9
# 1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16
# 1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25
# 1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36
# 1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49
# 1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64
# 1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81
#
# i = 1
# while i <= 9:
# #     j = 1
# #     while j <= i:
# #         a = i * j
# #         print('%s * %s = %s' % (j, i, a), end=(''))
# #         j += 1
# #     print()
# #     i += 1
# 4.求出1-100所有的质数(质数: 只能被1和它本身整除的数)
# i = 2
# while i <= 100:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         print('%s是质数' % (i), end=' ')
#     i += 1





