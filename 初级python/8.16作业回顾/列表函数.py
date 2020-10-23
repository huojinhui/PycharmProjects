# 列表作业:
# 1.调用列表操作的常用函数实现以下功能:
# 	- 1)创建一个空列表score
# 	- 2)在score列表中依次追加10个数值([68, 87, 92, 100, 76, 88, 54, 89, 76, 61] )
# 		extend()
# 		append()
# 	- 3)输出score列表中第3个元素的数值
# 	- 4)输出score列表中第1～6个元素的值
# 	- 5)在score列表第3个元素之前添加数值59
# 	- 6)利用变量num保存数值76，查询76分在score列表中出现的次数
# 	- 7)查询列表中是否有num76分的考试成绩
# 	- 8)查询score列表中成绩是满分的学生学号
# 	- 9)score列表中将59分加1分
# 	- 10)删除score列表中第1个元素
# 	- 11)获得score列表中元素的个数
# 	- 12)对列表中所有元素进行排序，输出考试的最高分和最低
# 	- 13)颠倒score列表中元素的顺序
# 	- 14)删除score列表中尾部的元素
# 	- 15)score列表中追加数值88，并输出。删除score列表中第一个数值88
# 	- 16)创建2个列表score1和score2,score1中包含数值2个元素值80,61,score2中包含3个元素值71,95,82，合并这两个列表，并输出全部元素
# 	- 17)创建score1列表，其中包含数值2个元素值80,61，将score1中元素复制5遍保存在score2列表中，输出score2列表中全部元素。
# 	score1 = [80,61]
# 	实现的代码...
# 	score2 = [80,61,80,61,80,61,80,61,80,61]
# 2.[68, 87, 92, 100, 76, 88, 54, 89, 76, 61] 去除列表中的偶数  --> [87,89,61]
# box = [68, 70, 92, 100, 76, 88, 54, 88, 76, 61]
# while True:
#     flage = True
#     for i in box:
#         if i % 2 == 0:
#             box.remove(i)
#             box = box
#             break
#             print(box)


# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)
# import random
# new = []
# red = list(range(1, 34))
# list_red = random.sample(red, 6)
# blue = random.randint(1, 16)
# new.extend(list_red)
# new.append(blue)
# print(new)


# 4.请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
# library = list(range(1, 103))
# a = []
# for i in range(len(library)):
#     new = []
#     if i % 3 == 0:
#         new.append(library[i])
#         if i + 1 < len(library):
#             new.append(library[i + 1])
#         if i + 2 < len(library):
#             new.append(library[i + 2])
#         a.append(new)
# print(a)


# 5. 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
# 	8  [1,2,3,4,5,8,6,7]
# 	3  [1,3,2]
# import random
# n = int(input('请输入一个数n:'))
# ran = list(range(1, n + 1))
# new = random.sample(ran, n)
# print(new)


# 附加题:
#
# 6.自己实现列表的sort方法 (排序算法)
#   [12,3123,123,3,4,354,3] --> [3,3,4,12..]6
# 选择拍序
# a = [12, 3123, 123, 3, 4, 354, 3]
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)
# 冒泡排序
# b = [12, 3123, 123, 3, 4, 354, 3]
# for i in range(len(b) - 1):
#     flage = True
#     for j in range(len(b) - 1 - i):
#         if b[j] > b[j + 1]:
#             b[j], b[j + 1] = b[j + 1], b[j]
#             flage = False
#     if flage == True:
#         break
# print(b)


# 7.写一个循环，不断的问用户想买什么，用户选择一个商品编号(下标)，就把对应的商品添加到购物车(列表)里，最终用户输入q退出时，打印购物车里的商品列表. 数据
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
#
# 结果: 输出买的所有商品名字,格式为:
# 	你购买的商品为: iphone8: 个数(count)	MacPro:个数...
# 	总价为: xx元
#
#
# 价格和商品名字一一对应
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799], ['wife', 10], ['wifi', 100000]]
# total_price = 0
# shopping_Cart = []
# while True:
#     try:
#         a = input('请输入相应的产品序号:')
#         if a == 'q' or a == 'Q':
#             print('退出系统')
#             break
#         elif int(a) < len(products):
#             a = int(a)
#             total_price += products[0][1]
#             print(products[a][0])
#             print('价格', products[a][1])
#             shopping_Cart.append(products[a][0])
#     except:
#         print('请重新输入')
# # print(shopping_Cart)
# print('总价:', total_price)
# # 对原来的购物车去重
# new_shopping_Cart = []
# for i in shopping_Cart:
#     if i not in new_shopping_Cart:
#         new_shopping_Cart.append(i)
#         # 计算商品的个数
#         new_shopping_Cart.append(shopping_Cart.count(i))
# print(new_shopping_Cart)