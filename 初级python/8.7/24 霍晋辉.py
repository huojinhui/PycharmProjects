# score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# 1.查询score列表中成绩是满分的所有的学生学号
# score = [68, 87, 92, 100, 100, 76, 100, 100, 88, 100, 54, 89, 76, 61]
# num = score.count(100)
# for i in range(len(score)):
#     if score[i] == 100:
#         print(i+1, end=' ')


# 2.删除score列表中所有的数值100
# score = [68, 87, 92, 100, 100, 76, 100, 100, 88, 100, 54, 89, 76, 61]
# new = []
# for i in score:
#     if i != 100:
#         new.append(i)
# print(new)


# 3.有一个字符串,凡是出现"|"和 " "和 "-"和"," 前后,就算一个单词. 计算下列字符串  str = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and" 单词的个数
# a = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# b = a.split("|")
# a = '+'.join(b)
# b = a.split(" ")
# a = '+'.join(b)
# b = a.split("-")
# a = '+'.join(b)
# b = a.split(",")
# a = '+'.join(b)
# b = a.split('+')
# print(len(b))


# 方法二
# a = a.replace('|', ' ').replace("-", ' ').replace(",", '')
# print(a.count(' '))


# 4.编写程序，完成以下要求：
# 	-  统计字符串中，各个字符的个数
# 	-  比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
# a = "hello world"
# b = a.replace(' ', '')
# new = []
# for i in b:
#     num = b.count(i)
#     if i not in new:
#         new.append(i)
#         print('%s:%s' % (i, num), end=' ')
# print(new)



# 5.给定一个带文件后缀名的字符串,要求: 将后缀名输出来 例如:  aasd.sad.sas.da?sdasdsaa.txt  --> txt
# a = 'aasd.sad.sas.da?sdasdsaa.py'
# new = a.split('.')
# print(new[len(new) - 1])

# 6.用户输入一堆字符串,打印出最后一个单词的长度 asdsa adasd asdsadas asdsadeasd asdsad
# str = input('请输入：')
# list = str.split()
# last = list[len(list) - 1]
# print(len(last))


# 7.用for循环打印一个菱形. 用center()做
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
# for i in range(1, 12, 2):
#     b = '*' * i
#     a = b.center(11)
#     print(a)
# for j in range(9, 0, -2):
#     b = '*' * j
#     a = b.center(11)
#     print(a)


# 8.要求用户输入字符串,计算一个字符串中所有英文字母的个数.'dsaas1232a1sdas12312dsadsadsadas'
# a = 'dsaas1232a1sdas12312dsadsadsadas'
# # num = []
# # english = []
# # for i in a:
# #     try:
# #         b = int(i)
# #         num.append(i)
# #     except:
# #         english.append(i)
# # print(len(num))
# # print(len(english))

# 9.模拟游戏聊天框,用户能一直输入内容,按回车,打印出用户输入的内容,但是,如果输入的内容当中,有敏感词汇,替换为 *
# 敏感词汇为:  ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
# zh = ['sb', 'SB', 'sB', 'Sb', '苍老师', '你大爷', '尼玛', '马化腾']
# while True:
#     a = input('用户输入:')
#     for i in zh:
#         if i in a:
#             a = a.replace(i, '*' * len(i))
#     print(a)
# 用户输入的内容为: 你是sb吗?你大爷的,做个人吧
#
# 打印的内容为: 你是**吗?***的,做个人吧
#
#
# 附加:
#
# 10.已知字符串 a = “aAsmr3idd4bgs7Dlsf9eAF”,要求如下
# 	- 请将a字符串的大写改为小写，小写改为大写。
# a = 'aAsmr3idd4bgs7Dlsf9eAF'
# b = a.swapcase()
# print(b)

# 	- 请将a字符串的数字取出，并输出成一个新的字符串。
# num = []
# english = []
# for i in a:
#     try:
#         b = int(i)
#         num.append(i)
#     except:
#         english.append(i)
# print(num)
# 用isdecimal判断

# 	- 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# a = 'abcabb'
# new = []
# for i in a:
#     if i not in new:
#         new.append(i)
# new = ''.join(new)
# print(new)


# 	- 请将a字符串反转并输出。例：’abc’的反转是’cba’
# 将字符串装换为列表,用列表反装函数
# a = 'aAsmr3idd4bgs7Dlsf9eAF'
# # b = ''
# # for i in range(len(a) - 1, -1, -1):
# #     b += a[i]
# # print(b)

# 	- 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
# 整体思路:先将字母排好序,然后判断字符串内有无字母
# a = 'aAsmr3idd4bgsBB7Dlsf9eAF'
# s = ''
# for i in a:
#     if i.isalpha():
#         s += i
# result = ''
# # chr(): 将数字转化为字母
# # 输出所有的大写字母
# for i in range(65, 91):
#     # 所有的大小写字母
#     # chr(i): 大写字母
#     # print(chr(i),chr(i + 32))
#     upper = chr(i) * s.count(chr(i))
#     lower = chr(i + 32) * s.count(chr(i + 32))
#     result += upper + lower
# print(result)


# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# a = 'aAsmr3idd4bgs7Dlsf9eAF'
# print('boy' in a)
# 	- 输出a字符串出现频率最高的字母
# a = 'aaaAsmr3idd4bgs7Dlsf9eAF'
# b = []
# c = []
# d = []
# e = []
# for i in range(len(a)):
#     b .append(a.count(a[i]))
# c .extend(b)
# b.sort()
# b.sort()
# max = b[len(b)-1]
# for j in range(len(c)):
#     if c[j] == b[len(b)-1]:
#         d.append(a[j])
# for i in d:
#     if i not in e:
#         e.append(i)
# print(e)


# 11.题目描述：
# 密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
# 假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
# 他是这么变换的，大家都知道手机上的字母： 1–1， abc–2, def–3, ghi–4, jkl–5, mno–6, pqrs–7, tuv–8 wxyz–9, 0–0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换
# 声明：
# 密码中没有空格,不能有标点符号，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
# 输入描述:
# 输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾；
# 输出描述:
# 输出渊子真正的密文
# 示例1：
# 输入：YUANzhi1987
# 输出：zvbo9441987
# while True:
#     a = input('请输入密码:')
#     if len(a) > 100:
#         print('请重新输入')
#     else:
#        break
# password = []
# for i in a:
#     if i.isdecimal() == True:
#         b = int(i)
#         password.append(i)
#     elif i.isupper() == True:
#         num = ord(i)
#         if num < 90:
#             xiaoxie = chr(num + 33)
#             password.append(xiaoxie)
#         elif num == 90:
#             xiaoxie = 'a'
#             password.append(xiaoxie)
#     elif i.islower() == True:
#         if i in 'abc':
#             password.append('2')
#         elif i in 'def':
#             password.append('3')
#         elif i in 'ghi':
#             password.append('4')
#         elif i in 'jkl':
#             password.append('5')
#         elif i in 'mno':
#             password.append('6')
#         elif i in 'pqrs':
#             password.append('7')
#         elif i in 'tuv':
#             password.append('8')
#         else:
#             password.append('9')
#     else:
#         print('格式错误,请重新输入')
#         break
# b = ''.join(password)
# print(b)


# 老师做的
import string
userInput = 'YUZN   zhi1987'
for i in userInput:
    if i in 'abc':
        userInput = userInput.replace(i,'2')
    elif i in 'def':
        userInput = userInput.replace(i, '3')
    elif i in 'ghi':
        userInput = userInput.replace(i, '4')
    elif i in 'jkl':
        userInput = userInput.replace(i, '5')
    elif i in 'mno':
        userInput = userInput.replace(i, '6')
    elif i in 'pqrs':
        userInput = userInput.replace(i, '7')
    elif i in 'tuv':
        userInput = userInput.replace(i, '8')
    elif i in 'wxyz':
        userInput = userInput.replace(i, '9')
# 把大写转化为小写
userInput = userInput.lower()
# 标点符号
biaodian = ' ,.+?<>/{}[]()!@#$%^&*:"'
# 结果
result = ''
for i in userInput:
    if i == 'z':
        result += 'a'
    elif i.isalpha():
        result += chr(ord(i) + 1)
    elif i not in string.punctuation and i != ' ':
        result += i
print(result)




