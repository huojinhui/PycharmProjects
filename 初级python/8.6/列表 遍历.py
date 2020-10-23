import random
a = ['霍晋辉', '是男男', '周文静', '白开心', '王海洋']
for i in range(0, len(a)):
    print(a[i])
for i in a:
    print(i)
a[1] = '史囡囡'
print(a)
b = random.randint(0, len(a)-1)
print(a[b])
