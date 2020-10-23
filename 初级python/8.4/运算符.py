# a=-10
# b=3
# print(b%a)
#     自己做的
#     cont=int(input('请输入一个三位数'))
#     bai=cont//100
#     ge=cont%10
#     shi=(cont-bai*100-ge)/10
#     he=bai+shi+ge
#     print((he))
        # 最佳解法
# cont=int(input("请输入一个三位数:"))
# bai=cont//100
# ge=cont%10
# shi=cont//10%10
# sum=bai**3+shi**3+ge**3
# print(sum)
#
#
# a=int(input('请输入第一个数:'))
# b=int(input('请输入第二个数:'))
# c=a+b
# print(c)
# a=True
# b=True
# c=(a)+(b)
# print(c,type(c),type(a))
a=1 and 2 and 0 and 4 and 5 or 6 or 7 or 8 and 9
print(a)
b=10 and 20
print(b)