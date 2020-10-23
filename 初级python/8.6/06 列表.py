# 空列表
a = []
print(type(a))
# 存储多个数据的列表
a = ['张三','李四','王五','赵六',10,20,50,True,False]
# 获取元素
# print(a[1])
# print(a[4])
# print(a)
# 设置(修改)元素值
# a[1] = 'aaa'
# a[100] = 'bbb'
# print(a)
a = ['张三','李四','王五','赵六',10,20,50,True,False,324,45,546,567678,7898,789,80808,435,43,65,756,8,7,9789,456,45,765,8767,867]

# 查看列表的长度
# print(len(a))
# 遍历: 将列表的每个元素取出来
# 通过下标遍历
# for i in range(0,len(a)):
#     print(a[i])
# 直接遍历列表的元素
# for i in a:
#     print(i)

a = ['霍金辉','是男男','周文静','白开心','蔡润建','王海洋','董延期']
# 1.用以上两种方式遍历
# 如果想修改列表当中元素的内容的话,只适合用下标的方式遍历
# for i in range(0,len(a)):
#     print(a[i])
#     # a[i] += 'a'
# # 不涉及到值的修改,使用这种方式
# for i in a:
#     i += 'a'
#     # print(i)
# print(a)
# 2.将 是男男 改为 史囡囡
# a[1] = '史囡囡'
# print(a)
# import random
# # 3.做一个随机抽奖,随机从列表a里面取一个名字,打印出来
# a = ['霍金辉','是男男','周文静','白开心','蔡润建','王海洋','董延期']
# num = random.randint(0,len(a) - 1)
# print(a[num])
#
# # 随机从列表当中获取元素
# print(random.choice(a))
# print(random.choices(a))

# 列表的嵌套: 一层一层取值
# 二维列表: 列表当中套了一层列表
a = [123,354,456,5476,[12,3345,56],[21324,565,7678,76],432,87,987]
print(a[4][0])
print(a[5][2])
# 三维
a = [123,354,456,5476,[12,[213354,6,65,67],3345,56],[21324,565,7678,76],432,87,987]
print(a[4][1][2])
# 超过三维一律称之为: 多维列表
# a = [123,354,456,5476,[12,[213,[213,12321,32,432],354,6,65,67],3345,56],[21324,565,7678,76],432,87,987]

