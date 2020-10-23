import random
# 1.调用列表操作的常用函数实现以下功能:
# 	- 1)创建一个空列表score
score = []
# 	- 2)在score列表中依次追加10个数值([68, 87, 92, 100, 76, 88, 54, 89, 76, 61] )
# 		extend()
score.extend([68, 87, 92, 100, 76, 88, 54, 89, 76, 61, 59])
# print(score)
# # #       append()
# # score.append(68)
# # score.append(87)
# # score.append(92)
# # score.append(100)
# # score.append(67)
# # score.append(88)
# # score.append(54)
# # score.append(89)
# # score.append(76)
# # score.append(61)
# # print(score)
# 	- 3)输出score列表中第3个元素的数值
# print(score[2])
# 	- 4)输出score列表中第1～6个元素的值
# for i in range(0, 6):
#     print(score[i])
# 	- 5)在score列表第3个元素之前添加数值59
# score.insert(2, 59)
# print(score)
# 	- 6)利用变量num保存数值76，查询76分在score列表中出现的次数
# num = score.count(76)
# print(num)
# 	- 7)查询列表中是否有num76分的考试成绩
# print(76 in score)
# 	- 8)查询score列表中成绩是满分的学生学号
# print(score.index(100)+1)
# 	- 9)score列表中将59分加1分
# result = score.count(59)
# print(result)
# for i in range(0, result):
#     score[score.index(59)] = score[score.index(59)] + 1
# print(score)




# print(score)
# 	- 10)删除score列表中第1个元素
# score.pop(0)
# print(score)
# 	- 11)获得score列表中元素的个数
# count = len(score)
# print(count)
# 	- 12)对列表中所有元素进行排序，输出考试的最高分和最低
# score.sort()
# print('最低分是:%s 最高分是:%s' % (score[0], score[len(score) - 1]))
# 	- 13)颠倒score列表中元素的顺序
# score.reverse()
# print(score)
# 	- 14)删除score列表中尾部的元素
# score.pop(len(score) - 1)
# print(score)
# 	- 15)score列表中追加数值88，并输出。删除score列表中第一个数值88
# score.append(88)
# print(score)
# loction = score.index(88)
# score.pop(loction)
# print(score)
# 	- 16)创建2个列表score1和score2,score1中包含数值2个元素值80,61,score2中包含3个元素值71,95,82，合并这两个列表，并输出全部元素
# score_1 = [80, 61]
# score_2 = [71, 95, 82]
# score_3 = []
# score_3.extend(score_1)
# score_3.extend(score_2)
# print(score_3)
# 	- 17)创建score1列表，其中包含数值2个元素值80,61，将score1中元素复制5遍保存在score2列表中，输出score2列表中全部元素。
# 	score1 = [80,61]
# 	实现的代码...
# 	score2 = [80,61,80,61,80,61,80,61,80,61]
# score1 = [80, 61]
# score2 = score1.copy() * 5
# print(score2)


# 2.[68, 87, 92, 100, 76, 88, 54, 89, 76, 61] 去除列表中的偶数  --> [87,89,61]
# old = [68, 87, 92, 100, 76, 88, 54, 89, 76, 61]
# new = []
# for i in old:
#     if i % 2 != 0:
#         new.append(i)
# print(new)


# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)
# new = []
# while True:
#     a = random.randint(1, 33)
#     if a not in new:
#         new.append(a)
#     if len(new) == 6:
#         break
# b = random.randint(1, 16)
# new.append(b)
# print(new)



# 4.请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
a = []
for i in range(1, 101):
    a.append(i)
print(a)
b = []
for i in range(1, 34):
    new = []
    new.append(a[0])
    new.append(a[1])
    new.append(a[2])
    b.append(new)
    for j in range(1, 4):
        a.pop(0)
b.append(a)
print(b)







# 5. 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
# 	8  [1,2,3,4,5,8,6,7]
# 	3  [1,3,2]
# n = int(input('请输入一个数:'))
# new = []
# while True:
#     a = random.randint(1, n)
#     if a not in new:
#         new.append(a)
#     if len(new) == n:
#         break
# print(new)
# 附加题:
#
# 6.自己实现列表的sort方法 (排序算法)
#   [12,3123,123,3,4,354,3] --> [3,3,4,12..]
# a = [12, 3123, 123, 3, 4, 354, 3]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# 7.写一个循环，不断的问用户想买什么，用户选择一个商品编号(下标)，就把对应的商品添加到购物车(列表)里，最终用户输入q退出时，打印购物车里的商品列表. 数据
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
# 结果: 输出买的所有商品名字,格式为:
# 	你购买的商品为: iphone8: 个数(count)	MacPro:个数...
# 	总价为: xx元
#
#
# 价格和商品名字一一对应
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799], ['wife', 10], ['wifi', 100000]]


                                                # while True:
                                                #     shangpin = []
                                                #     a = input('亲,请问您想买什么?(0----7)')
                                                #     if a == 'q':
                                                #         break
                                                #     else:
                                                #         b = int(a)
                                                #         shangpin = products[b][0]
                                                # print(shangpin)
