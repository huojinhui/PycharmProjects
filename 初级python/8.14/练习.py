
# # 浅复制
# a = [1, 2, 89]
# b = a
# b[0] = 20
# print(a, b)
#
# #深度复制
# import copy
# a = [[1, 2], 2, 89]
# b = a.copy()
# b.append(56)
# b[0][0] = 20
# print(a, b)
#
#
# # 和if一起使用
# a = [i for i in range(100) if i % 2 != 0]
# print(a)
#
#
# # 列表嵌套
# b = [j for i in range(8) for j in range(5)]
# print(b)
#
#
# # 和if   else一起使用
# c = [i ** 2 if i % 2 == 0 else i ** 4 for i in range(8)]
# print(c)



# 练习:
# a = [
#     {'name': 'aa','age': 80},
#     {'name': 'zs1','age': 30},
#     {'name': 'aasd32','age': 50},
#     {'name': 'zs12','age': 10},
#     {'name': 'zsaqew','age': 20},
#     {'name': 'zs213','age': 100},
#     {'name': 'zswer','age': 3}
# ]
# 1.使用def的函数的方式,取出大于20的数据,并且从小到大排序
#
# 2.使用匿名函数的方式,取出名字带有字母a的数据,并且从小到大排序
a = [
    {'name': 'aa', 'age': 80},
    {'name': 'zs1',' age': 30},
    {'name': 'aasd32', 'age': 50},
    {'name': 'zs12', 'age': 10},
    {'name': 'zsaqew', 'age': 20},
    {'name': 'zs213', 'age': 100},
    {'name': 'zswer', 'age': 3}
]
# def g(n):
#     # for n in a:
#     return n['age'] > 20
# res = list(filter(g, a))
# print(res)

# def f(n):
#     # 筛选条件
#     return n['age'] >= 20
#
# # 取出年龄大于50岁的数据
# result = list(filter(f,a))
#
# print(result)
# def f(n):
#     return n['age'] >= 20
# result = list(filter(f, a))
# print(result)


def f(n):
    return n['age'] >= 20
result = list(filter(f,a))
print(result)
# def g(n):
#     if n == 1:
#         return 1
#     return n * g(n - 1)
# print(g(5))
# def h(n):
#     if n == 2:
#         return n == 1
#     return h(n - 1) + h(n - 2)
# print(h(5))