# 方法一
# a=10
# b=20
# c=a
# a=b
# b=c
# print(a,b)
# 方法二
a=input('请输入第一个数:')
b=input('请输入第二个数:')
a,b=b,a
print(a,b)