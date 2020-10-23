import re, random
# -------机试题-------
#
#
# 1.	实现一个单例
# class Person:
#     def __init__(self, name, sex, height):
#         self.name = name
#         self.sex = sex
#         self.height = height
#     def eat(self):
#         print('%s吃饭了..'%(self.name))
#     def sleep(self):
#         print('%s正在睡觉'%(self.name))
# p = Person('张三','男',180)
# p.eat()
# p.sleep()
# p1 = Person('李四', '女', 160)
# p1.eat()
# p1.sleep()


# 2.	实现冒泡,选择排序
# a = [9, 3, 5, 6, 6, 56, 25]
# # 选择排序
# for i in range(len(a) - 1):
#     for j in range(len(a) - i):
#         if a[i] > a[i + j]:
#             a[i], a[i + j] = a[i + j], a[i]
# print(a)
#
# # 冒泡排序
# for i in range(len(a) - 1):
#     flag = True
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#         flag = False
#     if flag == True:
#         break
# print(a)


# 3.	输出1-100间的所有质数
# for i in range(2, 101):
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         print('{}是质数'.format(i))


# 4.	逗号隔开输入某年某月某日，判断这一天是这一年的第几天？
# 例如: 输入: 2004,3,1 输出: 61
# 	  输入: 2005,3,1 输出: 60
# years = input('请输入年份:')
# b = years.split(',')
# year = int(b[0])
# mouth = int(b[1])
# day = int(b[2])
# # print(mouth)
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('闰年')
#     if mouth % 2 == 0:
#         count = (mouth - 1) * 30 + mouth/2 - 2 + day
#         print(count)
#     else:
#         count = (mouth - 1) * 30 + (mouth - 1)/2 - 1 + day
#         print(count)
# else:
#     print('平年')
#     if mouth % 2 == 0:
#         count = (mouth - 1) * 30 + mouth/2 - 3 + day
#         print(count)
#     else:
#         count = (mouth - 1) * 30 + (mouth - 1)/2 - 2 + day
#         print(count)


# 5.	一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# height = 100
# mi = 100
# for i in range(1, 11):
#     height = height / 2
#     print(height)
#     if i == 1:
#         mi = 100
#         print(mi)
#     else:
#         mi = height * 4 + mi
#         print(mi)


# 6.	将字符串"a-b-c-d-e-f"倒叙输出,中间字符变为大写: “f-e-d-C-b-a”

# 7.	实现函数strip,要求自己实现去除字符串首尾空格的功能
# 输入: ‘hello     ’  输出: ‘hello’
# 输入: ‘h   ello     ’  输出: ‘h   ello’
# 输入: ‘   hello     ’  输出: ‘ hello’
# a = '‘h   ello     ’'
# pattern = r'[a-z0-9]{1}.+[a-z0-9]{1}'
# b = re.findall(pattern, a)
# print(b[0])


# 8.	功能描述：删除字符串中字符个数最少的字符，而且最少字符串有多个，最少的要全部删除 然后返回该字符串
# 输入：asdasdasbb
# 输出：asasas
# word = 'asdasdasbb'
# frequency_occurrence = []
# for i in range(len(word)):
#     num = word.count(word[i])
#     frequency_occurrence.append(num)
# small = min(frequency_occurrence)
# yuansu = []
# a = 0
# while a < len(frequency_occurrence):
#     a = frequency_occurrence.index(small, a)
#     yuansu.append(word[a])
#     a += 1
# for i in yuansu:
#     word = word.replace(i, '')
# print(word)



# 9.	随机生成，100个从1到10的随机整数，然后每个偶数出现的次数:
# 例如: 1,2,3,2,3,1,5,6,10,2
# 输出: {“2”: 3,”6”: 1 “10”: 1}
# num = []
# # 做出随机数
# for i in range(100):
#   num.append(random.randint(1, 10))
# # print(num)
# # 去重
# new = []
# dic = {}
# for j in num:
#     if j % 2 == 0:
#         if j not in new:
#             new.append(j)
#             dic[j] = num.count(j)
# print(dic)

# 10.	用户输入日期,判断是否为日期,格式如下: 2018-12-6,年份1-9999,月份01-12或者1-12,天数01-31或者1-31,不用考虑每个月的具体天数,例如: 2018-2-31也满足
# date = input('请输入日期:')
# if date.count('-') == 2:
#     year = int(date[:date.index('-') + 1])
#     mouth = date[date.rfind('-'):date.rindex('-') + 1]
#     day = date[date.rfind('-'):]
#     if year >= 1  and year <= 9999:
#         if len(mouth) == 1:
#             if int(mouth) >= 1 and int(mouth) <= 9:
#                 if day[0] == '0':
#                     if int(day[1]) >= 1  and int(day[1]) <= 9:
#                         print('格式真确')
#                     else:
#                         print('格式错误')
#                 else:
#                     if int(day[1]) >= 1  and int(day[1]) <= 31:
#                         print('格式真确')
#                     else:
#                         print('格式错误')
#         elif len(mouth) == 2:
#             if mouth[0] == '0':
#                 if int(mouth[1]) >= 1  and int(mouth[1]) <= 9:
#                     if day[0] == '0':
#                         if int(day[1]) >= 1 and int(day[1]) <= 9:
#                             print('格式真确')
#                         else:
#                             print('格式错误')
#                     else:
#                         if int(day[1]) >= 1 and int(day[1]) <= 31:
#                             print('格式真确')
#                         else:
#                             print('格式错误')
#             else:
#                 if int(mouth) >= 1 and int(mouth) <= 12:
#                     if day[0] == '0':
#                         if int(day[1]) >= 1 and int(day[1]) <= 9:
#                             print('格式真确')
#                         else:
#                             print('格式错误')
#                     else:
#                         if int(day[1]) >= 1 and int(day[1]) <= 31:
#                             print('格式真确')
#                         else:
#                             print('格式错误')
#         else:
#             print('格式不对')
#
#     else:
#         print('格式不对')
# else:
#     print('格式不对')