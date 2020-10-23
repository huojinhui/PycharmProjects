# 选则排序
# a = [200, 5, 1, 2, 8, 9, 5, 8, 7, 78, 56, 100]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)
# for i in range(len(a)):
#     print(a[i])
# for i in a:
#     print(i)



# 常规冒泡排序
# a = [200, 5, 1, 2, 8, 9, 5, 8, 7, 78, 56, 100]
# for i in range(len(a) - 1):
#     # print(i)
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#     print(a)


# 优化冒泡排序
import random
n = int(input('请输入一个数:'))
new = []
while True:
    a = random.randint(1, n)
    if a not in new:
        new.append(a)
    if len(new) == n:
        break
print(new)
a = [200, 5, 1, 2, 8, 9, 5, 8, 7, 78, 56, 100]
a.extend(new)
for i in range(len(a) - 1):
    flag = False
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = True
    if flag == False:
        break
print(a)


# a = [200, 5, 1, 2, 8, 9, 5, 8, 7, 78, 56, 100]
# for i in range(len(a)):
# #     for j in range(i + 1, len(a)):
# #         if a[i] > a[j]:
# #             a[i], a[j] = a[j], a[i]
# # print(a)


# for i in range(len(a) - 1):
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#         print(a)

# for i in range(len(a) - 1):
#     b = 0
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             b = 1
#     if b == 0:
#         break
# print(a)


# a = [200, 5, 1, 2, 8, 9, 5, 8, 7, 78, 56, 100]
# for i in range(len(a) - 1):
#     b = 0
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             b = 1
#     if b == 0:
#         break
# print(a)