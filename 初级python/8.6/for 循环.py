# for i in range(1, 10, -1):
#     print(i)
# sum = 0
# for i in range(1, 1001):
#     if i % 3 == 0 or i % 17 == 0:
#         sum += i
# print(sum)
#
#
# ji = 1
# for i in range(1, 11):
#     ji *= i
#     print('%s的阶乘为:%s' % (i, ji))
#     print()
#
#
# ji = 1
# he = 0
# for i in range(1,11):
#     ji *= i
#     he += ji
# print(he)


# for i in range(3, 0, -1):
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
# print('失去登陆机会,明天再来.')


# for i in range(100, 1000):
#     bai = i // 100
#     ge = i % 10
#     shi = i // 10 % 10
#     count = bai ** 3 + shi ** 3 + ge ** 3
#     if count == i:
#         print(count)



# cunt = 0
# for i in range(10000, 100001):
#     one = i // 10000
#     two = int(i // 1000) % 10
#     three = int(i // 100) % 10
#     four = int(i // 10) % 10
#     five = i % 10
#     if one == five and two == four:
#         print(i)
#         cunt += 1
# print(cunt)

# he = 1
# for i in range(1, 7):
#     he = (he + 1) * 2
#     print(he)
# print(he)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()


# kongge = 3
# for i in range(1, 8, 2):
#     print(' ' * kongge, end='')
#     print('*' * i)
#     kongge -= 1
# kongge = 1
# for i in range(5, 0, -2):
#     print(' '*kongge, end='')
#     print('*' * i)
#     kongge += 1

# for i in range(1, 10):
#     for j in range(1, i):
#         a = i * j
#         print('%s * %s = %s' % (j, i, a), end='\t')
#     print()


# 4.求出1-100所有的质数(质数: 只能被1和它本身整除的数)
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print('%s是质数'%(i))