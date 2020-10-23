# 0.写函数,传入一个参数n,返回n的阶乘的结果
# 例如: cal(5)  返回的结果为: 5 * 4 * 3 *  2 * 1
# def jiecheng(n):
#     ji = 1
#     for i in range(1, n + 1):
#         ji *= i
#     print()
#     return ji
# n = int(input('请输入一个数:') )
# print(jiecheng(n))

# 1.写函数,要求传入列表或者元组,取得下标为偶数的值作为新的列表或者元组,返回给调用者
# def qiuou(*args):
#     a = []
#     if type(args[0]) == list:
#         for i in range(len(args[0])):
#             if i % 2 == 0:
#                 a.append(args[0][i])
#         return a
#     else:
#         b = list(args)
#         for i in range(len(b)):
#             if i % 2 == 0:
#                 a.append(b[i])
#                 c = tuple(a)
#         return c
# print(qiuou(1, 2, 3))
# def a(n):
#     return n[0::2]
# print(a(1, 2, 3))


# 2.写函数,判断用户传入的对象(字符串,列表,元组)长度是否大于5
# def long(args):
#     if len(args) > 5:
#         print('对象长度大于5')
#     else:
#         print('对象长度小于等于5')
# a = (1, 4, 5, 8, 8, 58)
# print(long(a))

# 方法2
# def length(n):
#     if len(n) > 5:
#         return True
#     return False

# 3.写函数,检查列表的长度,如果大于5,则将列表的前5项内容返回给调用者
# 可以用切片
# [12312,32,4,234234,23,432432,4,23] return [12312,32,4,234234,23]
# def long(a):
#     b = []
#     if len(a) > 5:
#         print('对象长度大于5')
#         for i in range(5):
#             b.append(a[i])
#         return b
#     else:
#         print('对象长度小于等于5')
# a = [12312,32,4,234234,23,432432,4,23]
# print(long(a))
# 优化  可以直接用切片
# def b(n):
#     if len(n) > 5:
#         return n[:6]


# 4.写函数,要求传入一个字符串,统计每个字符出现的次数,将其制作为字典返回给调用者
# wekwqekj  {'w': 2,'e': 2,'k': 2..}
# def cishu(a):
#     # 放最后结果的字典
#     b = {}
#     # 放去重后的字符
#     c = []
#     # 去掉重复的字符
#     for i in a:
#         if i not in c and i != ' ':
#             c.append(i)
#     # 将去重的字符和其出现的次数加到一个新字典里
#     for j in c:
#         b[j] = a.count(j)
#     return b
# a = 'wekwqekj '
# print(cishu(a))
# 优化
# def count(n):
#     a = ''
#     dic = {}
#     for i in n:
#         if i not in a and i != ' ':
#             a += i
#             dic[i] = n.count(i)
#     return dic

# 5.写函数,接收三个参数,返回值较大的那个数字
# a = [1, 2, 3]
# def da(a):
#     max = a[0]
#     for i in a:
#         if i > max:
#             max = i
#     return max
# print(da(a))


# 6.写函数,检查传入字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容,并组合为新字典返回给调用者
# 例如:
# 传入:
# 	dic = {'k1': 'v1v2','k2': [11,22,33,44]}
# 返回:
# 	dic {'k1': 'v1','k2': [11,22]}
# 假定value只能是列表或者字符串
# def hanshu(dic):
#     # 遍历dic中的key
#     for i in dic.keys():
#         # 判断value的leix
#         if type(dic[i]) == list:
#             # 做一个空列表接受返回值
#             new = []
#             # 如果列表长度大于二截取前2个返回new
#             if len(dic[i]) > 2:
#                 # 遍历value去前俩
#                 for j in range(2):
#                     new.append(dic[i][j])
#                 dic[i] = new
#         # value值为字符是
#         if type(dic[i]) == str:
#             new = ''
#             if len(dic[i]) > 2:
#                 for j in range(2):
#                     new += dic[i][j]
#                 dic[i] = new
#     return dic
# dic = {'k1': 'v1v2', 'k2': [11, 22, 33, 44]}
# print(hanshu(dic))
# 优化


#
#
#
# 比名片系统难一些(所有知识点的整合,列表,字符串,字典,函数)
#
# 双色球彩票系统: 6个功能全部封装成函数.
#
# # 自己的余额自己设置
# price = 10000
#
# [{'red': 红球列表,'blue': 蓝球},{'red': 红球列表,'blue': 蓝球}]
#
# 彩票: {
# 	'red': [],
# 	'blue': int
# }
#
# 一张彩票:
# {'red': [],'blue': int}
#
# 所有的彩票:[{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int}]
#
#
# - 从1-33共33个红色号码球中选择6个号码，并从1-16共16个蓝色号码球中选择1个号码
#
#
# - 交互大框架 （原始金额自定，彩票2元一张）
# ==================================================
#    双色球 V0.01
#  1. 充值  （先显示原有金额，再输入金额，最后显示充值后的金额）
#  2. 随机生成一个彩票 (显示生成的彩票: 红球: 12... 蓝球: 蓝球号码)
#  3. 手动输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): 1,2,3,4,5,6,7
#  4.查看最新一期彩票结果, 显示开奖后的账户余额 （最新一期彩票结果随机产生）
#  	格式:
#  	本期彩票的结果为: 红球: 1,2,3,4,5,6 蓝球: 1
#  	中6+1 奖金1000万
#  	中5+0 奖金200
#  	...
#  	...
#  	...
#  	最终账户余额为: xxxx
#  5. 显示当前余额
#  6. 显示所有的彩票:
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  			红球: 6个数字  蓝球: 1
#  7.	退出系统
# ==================================================
#     请输入操作序号:
price = 100
lottery_pool = []
def show(a):
    red = a['红球']
    blue = a['蓝球']
    result = []
    for i in red:
        i = str(i)
        result.append(i)
    jieguo = ','.join(result)
    print('红球: ', jieguo, '蓝球', blue)
while True:
    instructions = input('''
    1. 充值
    2. 随机生成一个彩票
    3. 手动输入彩票号码 
    4.查看最新一期彩票结果
    5. 显示当前余额
    6. 显示所有的彩票
    7.	退出系统
    请输入操作序号:
    ''')
    if instructions == '1':
        import string
        print('余额为%s,钱不多了,再充点吧' % (price))
        a = input('请问充吗?(建议你多重点)')
        if a in '充是冲重':
            qian = int(input('充多少:'))
            price = qian + price
            print('余额为%s' % (price))
            print('充值成功,希望下次多重点')
        if a in '不否':
            print('不充就走,别烦我')
    if instructions == '2':
        if price < 2:
            print('没钱了,去重点b吧')

        else:
            import random
            red = list(range(1, 34))
            red = random.sample(red, 6)
            blue = random.randint(1, 16)
            new_lottery = {
                '红球': red,
                '蓝球': blue
            }
            print('一张彩票')
            show(new_lottery)
            print('生成成功')
            price -= 2
            lottery_pool.append(new_lottery)
            # if price < 2:
            #     print('没钱了,去重点b吧')
            #     break
    if instructions == '3':
        if price < 2:
            print('没钱了,去重点b吧')
        else:
            red = []
            i = 1
            while i <= 6:
                a = input('请输入红球号码第%s位:' % (i))
                b = string.punctuation
                if a == ' ' or a in b:
                    if int(a) > 33:
                        print('输入太大,请重输:')
                        continue
                    if a not in red:
                        red.append(a)
                        i += 1
                    else:
                        print('输入重复,请冲输入:')
                else:
                    print('xia')
            print(red)
            while True:
                blue = int(input('请输入蓝球:'))

                if blue > 16:
                    print('冲输入:')
                else:
                    break
            print(blue)
            new_lottery = {
                '红球': red,
                '蓝球': blue
            }
            print('一张彩票')
            show(new_lottery)
            lottery_pool.append(new_lottery)
            price -= 2
    if instructions == '4':
        import random
        red = list(range(1, 34))
        red = random.sample(red, 6)
        blue = random.randint(1, 16)
        lottery_results = {
            '红球': red,
            '蓝球': blue
        }
        print('本期彩票的结果为')
        print('红球:', lottery_results['红球'])
        print('蓝球:', lottery_results['蓝球'])

        for i in lottery_pool:
            red_count = 0
            for j in i['红球']:
                if j in lottery_results['红球']:
                    red_count += 1
            # print(red_count)
            if i['蓝球'] == lottery_results['蓝球']:
                blue_count = 1
            else:
                blue_count = 0
            # print(blue_count)
            if red_count == 6:
                if blue_count == 1:
                    print('中一等奖10000000')
                    price += 10000000
                if blue_count == 0:
                    print('中二等奖5000000')
                    price += 5000000
            if red_count == 5:
                if blue_count == 1:
                    print('中3等奖3000')
                    price += 3000
                if blue_count == 0:
                    print('中4等奖200')
                    price += 200
            if red_count == 4:
                if blue_count == 1:
                    print('中4等奖200')
                    price += 200
                if blue_count == 0:
                    print('中5等奖10')
                    price += 10
            if blue_count == 1:
                if red_count == 3:
                    print('中5等奖10')
                    price += 10
                if red_count == 2:
                    print('中6等奖5')
                    price += 5
                if red_count == 1:
                    print('中6等奖5')
                    price += 5
            else:
                print('没中奖,好可惜')
        print('最终账户余额为%s'%(price))
    if instructions == '5':
        print(price)
    if instructions == '6':
        for i in lottery_pool:
            show(i)
    if instructions == '7':
        print('退出成功')
        break
    else:
        print('请输入正确的序号')