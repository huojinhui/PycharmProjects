# 0.实现简易计算器功能,如图
a = int(input('请输入第一个数:'))
b = int(input('请输入第二个数:'))
c = str(input('请输入要做的运算(+,-,*,/):'))
if c == "+":
    sum = a+b
    print(sum)
else:
    if c == "-":
        sum = a-b
        print(sum)
    else:
        if c == '*':
            sum = a*b
            print(sum)
        else:
            if c == '/':
                sum = a/b
                print(sum)
            else:
                sum = a + b
                print(sum)

# 1.让用户输入两个任意的整数, 比较两个数的大小, 输出最大的数
a = input('请输入第一个整数:')
b = input('请输入第二个整数:')
if a > b:
    print(a)
else:
    print(b)


# 2.用户输入一个数,打印出奇数还是偶数
a = int(input('请输入一个数:'))
if a % 2 == 0:
    print('偶数')
else:
    print('奇数')


# 3.用户输入帐号密码,帐号为admin,密码为8888显示登录成功,其余的显示登录失败
id = input('账号:')
password = input('密码:')
# 注意数字类型
if id == 'admin' and password == '8888':
    print('登陆成功')
else:
    print('登陆失败')


# 4.用户输入一个三位数,输出结果是否为水仙花数(水仙花数: 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。)
cont = int(input("请输入一个三位数:"))
bai = cont//100
ge = cont % 10
shi = cont//10 % 10
sum = bai ** 3+shi ** 3+ge ** 3
if sum == cont:
    print('是水仙花数')
else:
    print('不是水仙花数')


# 5.用户输入年份,输出结果是闰年还是平年(闰年: 1.能整除4且不能整除100 2.能整除400)
year = int(input('请输入年份'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('闰年')
else:
    print('平年')


# 6.输入公交卡当前的余额,空座位数，只要超过2元，就可以上公交车;没钱,撵走；如果空座位的数量大于0，就可以坐下;
a = int(input('请输入当前余额:'))
if a >= 2:
    print('上车')
    b = int(input('请输入空座位数:'))
    if b > 0:
        print('坐下')
    else:
        print('站着')
else:
    print('撵走')


# 7.
# 成绩等级:
# 90
# 分以上: 等级为A
#
# 80 - 90: 等级为B
#
# 60 - 80: 等级C
#
# 0 - 60: 等级为D
date = int(input('请输入成绩:'))
if date >= 90:
    print('等级A')
elif date >= 80:
     print('等级B')
elif date >= 60:
    print('等级C')
else:
    print('等级D')


# 8.场景应用: 上火车 (用户输入表示是否有票,是否有刀具)
# 	是否有票,有票打印可以进站;
# 	进站查看是否带有刀具,有刀具,没收上车,没有刀具,直接上车
# 	没票打印不可以进站
a = input('是否有票:')
if a == '是':
    print('进站')
    b = input('是否有刀:')
    if b == '是':
        print('没收上车')
    else:
        print('上车')
else:
    print('不可以进站')


# 9.女友的节日:
# 	定义holiday_name字符串变量记录节日名称
# 	如果是 情人节 应该 买玫瑰／看电影
# 	如果是 平安夜 应该 买苹果／吃大餐
# 	如果是 生日 应该 买蛋糕
# 	其他的时候,每天都是节日
holiday_name = input('请输入节日:')
if holiday_name == '情人节':
    print('买玫瑰／看电影')
elif holiday_name == '平安夜':
    print('买苹果／吃大餐')
elif holiday_name == '生日':
    print('买蛋糕')
else:
    print('每天都是节日')


# 10.英雄联盟(LOL)李青技能:
# 	q,Q:天音波
# 	w,W:金钟罩/铁布衫
# 	e,E:天雷破/摧筋断骨
# 	r,R:猛龙摆尾
a = input('请输入技能:')
if a == 'q' or a == 'Q':
    print('天音波 ')
elif a == 'e' or a == 'E':
    print('金钟罩/铁布衫')
elif a == 'W' or a == 'w':
    print('天雷破/摧筋断骨')
else:
    print('猛龙摆尾')


# 11.用户决定是否发工资,工资数是多少,信用卡欠款;有剩余的时候,显示剩余金额(图1)
a = input('今天发工资吗?')
if a == 'yes':
    print('先还信用卡的钱')
    b=input('还有剩余吗?')
    if b == 'yes':
        print('又可以Happy了')
    else:
        print('奥,no')
else:
    print("盼工资")
#

# 12.让用户输入三个任意的整数, 比较三个数的大小, 输出最大的数
a = int(input('请输入第1个数:'))
b = int(input('请输入第2个数:'))
c = int(input('请输入第3个数:'))
if a > b > c or a > c > b:
    print(a)
else:
    if b > a > c or b > c > a:
        print(b)
    else:
        print(c)


        # a = int(input('请输入第一个数'))
        # b = int(input('请输入第二个数'))
        # c = int(input('请输入第三个数'))
        # # 将a赋值给变量max,假设max为最大值
        # max = a
        # # 如果b比max大，把b赋值给max
        # if b > max:
        #     max = b
        # # 如果c比max大，把c赋值给max
        # if c > max:
        #     max = c
        #  # 输出最大值max
        # print(max)


# 10.英雄联盟(LOL)李青技能:
# 	q,Q:天音波
# 	w,W:金钟罩/铁布衫
# 	e,E:天雷破/摧筋断骨
# 	r,R:猛龙摆尾
# 技能
skill = input('输入技能: ')
if skill in 'qQ':
    print('天音波')
if skill in 'wW':
    print('金钟罩/铁布衫')
if skill in 'eE':
    print('天雷破/摧筋断骨')
if skill == 'q' or skill == 'Q':
    print('天音波')
if skill == 'w' or skill == 'W':
    print('金钟罩/铁布衫')
if skill == 'e' or skill == 'E':
    print('天雷破/摧筋断骨')