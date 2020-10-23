price = 0
lottery_pool = []
# 去重
def quchong(new_lottery, lottery_pool):
    global price
    new_lottery = {'红球': [30, 20, 23, 18, 32, 10], '蓝球': 4}
    for i in lottery_pool:
        red_count = 0
        for j in i['红球']:
            if j in new_lottery['红球']:
                red_count += 1
        # print(red_count)
        if i['蓝球'] == new_lottery['蓝球']:
            blue_count = 1
        else:
            blue_count = 0
        if red_count == 6 and blue_count == 1:
            print('该彩票重复了')
            return None
        else:
            print('一张彩票')
            print(new_lottery)
            print('生成成功')
            price -= 2
            lottery_pool.append(new_lottery)
# 查询余额
def recharge():
    global  price
    print('余额为%s,钱不多了,再充点吧' % (price))
    a = input('请问充吗?(建议你多重点)')
    if a in '充是冲重':
        qian = int(input('充多少:'))
        price = qian + price
        print('余额为%s' % (price))
        print('充值成功,希望下次多重点')
    if a in '不否':
        print('不充就滚,别烦我')
# 随机生成一个彩票
def Random_lottery():
    global price
    import random
    red = list(range(1, 34))
    red = random.sample(red, 6)
    blue = random.randint(1, 16)
    new_lottery = {
        '红球': red,
        '蓝球': blue
    }
    # quchong(new_lottery, lottery_pool)
    print('一张彩票')
    print(new_lottery)
    print('生成成功')
    price -= 2
    lottery_pool.append(new_lottery)
def show(a):
    red = a['红球']
    blue = a['蓝球']
    print(red, blue)
    result = []
    for i in red:
        i = str(i)
        result.append(i)
    jieguo = ','.join(result)
    print('红球: ', jieguo, '蓝球', blue)
def input_lottery():
    import string
    global price
    if price < 2:
        print('没钱了,去重点b吧')
    else:
        red = []
        i = 1
        while i <= 6:
            a = input('请输入红球号码第%s位:' % (i))
            b = string.punctuation
            if a == '' or a in b:
                print('请不要瞎胡写')
            else:
                try:
                    if int(a) > 33:
                        print('输入太大,请重输:')
                        continue
                    if a not in red:
                        red.append(a)
                        i += 1
                    else:
                        print('输入重复,请输冲入:')
                except:
                    print('不要乱输')
        print(red)
        while True:
            blue = int(input('请输入蓝球号码:'))

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
def winning_results():
    global price
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
    print('最终账户余额为%s' % (price))
def show_balance():
    global price
    print(price)
def show_all_lottery():
    for i in lottery_pool:
        show(i)

while True:
    instructions = input('''
    1. 充值
    2. 随机生成一个彩票
    3. 手动输入彩票号码 
    4. 查看最新一期彩票结果
    5. 显示当前余额
    6. 显示所有的彩票
    7.	退出系统
    请输入操作序号:
    ''')
    if instructions == '1':
        recharge()
    if instructions == '2':
        Random_lottery()
    if instructions == '3':
        input_lottery()
    if instructions == '4':
        winning_results()
    if instructions == '5':
        show_balance()
    if instructions == '6':
        show_all_lottery()
    if instructions == '7':
        print('退出成功')
        break
    else:
        print('请输入正确的序号')

