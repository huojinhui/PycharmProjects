# score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# 1.查询score列表中成绩是满分的所有的学生学号
# count = 0
# score = [68, 87, 92, 100, 100, 76, 100, 100, 88, 100, 54, 89, 76, 61]
# for i in range(len(score)):
#     if score[i] == 100:
#         count = score.index(100, count)
#         print(count)
#         count += 1


# 2.删除score列表中所有的数值100
# score = [68, 87, 92, 100, 100, 76, 100, 100, 88, 100, 54, 89, 76, 61]
# for i in range(score.count(100)):
#     score.remove(100)
# print(score)


# 3.有一个字符串,凡是出现"|"和 " "和 "-"和"," 前后,就算一个单词. 计算下列字符串  str = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and" 单词的个数
str = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# new = str.replace(" ", "|").replace("-", "|").replace(",", "|")
# print(new)
# b = new.split('|')
# print(len(b))

# 4.编写程序，完成以下要求：
# 	-  统计字符串中，各个字符的个数
# 	-  比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
# a = "hello world"
# a = a.replace(' ', '')
# b = ''
# for i in a:
#     if i not in b:
#         b += i
# for j in b:
#     print(j, b.count(j))


# 5.给定一个带文件后缀名的字符串,要求: 将后缀名输出来 例如:  aasd.sad.sas.da?sdasdsaa.txt  --> txt
# a = 'aasd.sad.sas.da?sdasdsaa.txt'
# b = a[a.rfind('.') + 1:]
# print(b)


# 6.用户输入一堆字符串,打印出最后一个单词的长度 asdsa adasd asdsadas asdsadeasd asdsad
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
#     a = '*' * i
#     b = a.center(11)
#     print(b)
# for j in range(9, 0, -2):
#     a = '*' * j
#     b = a.center(11)
#     print(b)


# 8.要求用户输入字符串,计算一个字符串中所有英文字母的个数.'dsaas12312asdas12312dsadsadsadas'
# a = 'dsaas12312asdas12312dsadsadsadas'
# number = 0
# for i in a:
#     b = a.isalpha()
#     if b == False:
#         number += 1
# print(number)


# 9.模拟游戏聊天框,用户能一直输入内容,按回车,打印出用户输入的内容,但是,如果输入的内容当中,有敏感词汇,替换为 *
# 敏感词汇为:  ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']

# 示例:
# 用户输入的内容为: 你是sb吗?你大爷的,做个人吧
#
# 打印的内容为: 你是**吗?***的,做个人吧

# 此方法会替换过多,应把列表中的元素当成整体替换
# sensitive_words = ['sb', 'SB', 'sB', 'Sb', '苍老师', '你大爷', '尼玛', '马化腾']
# sensitive_words = ','.join(sensitive_words)
# user = input('输入:')
# for i in user:
#     if i in sensitive_words:
#         user = user.replace(i, '*')
# print(user)


#优化
# a = ['sb', 'SB', 'sB', 'Sb', '苍老师', '你大爷', '尼玛', '马化腾']
# while True:
#     # 用户输入内容
#     # userInput = '你是sb吗?你大爷的,做个人吧'
#     userInput = input('请输入聊天内容: ')
#     # 判断每一个敏感词汇是否在用户输入的内容当中,如果存在,则替换
#     for i in a:
#         if i in userInput:
#             userInput = userInput.replace(i, '*' * len(i))
#     print(userInput)


# 附加:
#
# 10.已知字符串 a = “aAsmr3idd4bgs7Dlsf9eAF”,要求如下
# 	- 请将a字符串的大写改为小写，小写改为大写。
# 	- 请将a字符串的数字取出，并输出成一个新的字符串。
# 	- 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# 	- 请将a字符串反转并输出。例：’abc’的反转是’cba’
# 	- 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# 	- 输出a字符串出现频率最高的字母
# a = 'aAsmr3idd4bgs7Dlsf9eAFas'
# # 将字母取出放在一个新字符串里
# new = ''
# for i in a:
#     if i.isalpha():
#         new += i
# # 将字母都变成小写返回new
# new = new.lower()
# # number放每个字母出现的次数
# number = []
# for i in range(len(new)):
#     number.append(new.count(new[i]))
# # b表示最高次数
# b = max(number)
# # count用来计数
# count = 0
# # chongfu放出现频率最高的字母但没有去重
# chongfu = ''
# # 根据下标相同的道理取出次数最高的字母
# for i in range(len(number)):
#     if number[i] == b:
#         xiabiao = number.index(b, count)
#         count += 1
#         chongfu += new[xiabiao]
# # result放最后的结果
# result = ''
# # 去重
# for i in chongfu:
#     if i not in result:
#         result += i
# print(result)


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
# 提示文字
# print('密码中没有空格,不能有标点符号')
# password = input('请输入密码:')
# # 空字符放新密码
# encryption = ''
# for i in password:
#     # 如果是小写变成数字
#     if i.islower():
#         if i in 'abc':
#             encryption += '2'
#         elif i in 'def':
#             encryption += '3'
#         elif i in 'ghi':
#             encryption += '4'
#         elif i in 'jkl':
#             encryption += '5'
#         elif i in 'mno':
#             encryption += '6'
#         elif i in 'pqrs':
#             encryption += '7'
#         elif i in 'tuv':
#             encryption += '8'
#         elif i in 'wxyz':
#             encryption += '9'
#     # 如果是大写
#     elif i.isupper():
#         # 如果是90直接变成a
#         if ord(i) == 90:
#             daxie = 'a'
#         else:
#             # 转化成数字然后+33然后转化成字母
#             daxie = chr(ord(i) + 33)
#             encryption += daxie
#     # 直接变成数字
#     elif i.isdecimal():
#         encryption += i
#     else:
#         print('格式有误,请重新输入')
#         break
# print('请输出密码:', encryption)
