# 0.
# 任意选取豆瓣电影top250的5条数据用数据类型表示出来(字典和列表的组合列表包5个字典)
# a1 = {
#     '电影名': '肖申克的救赎',
#     '导演': ['弗兰克·德拉邦特', 'Frank Darabont '],
#     '主演': ['蒂姆·罗宾斯', 'Tim Robbins'],
#     '评分': '9.7',
#     '评论': '希望让人自由'
# }
# a2 = {
#     '电影名': '霸王别姬',
#     '导演': ['陈凯歌', 'Kaige Chen '],
#     '主演': ['张国荣', 'Leslie', '张丰毅', 'Fengyi Zha'],
#     '评分': '9.6',
#     '评论': '风华绝代。'
# }
# a3 = {
#     '电影名': '盗梦空间',
#     '导演': ['克里斯托弗·诺兰 ', 'Christopher Nolan'],
#     '主演': '莱昂纳多·迪卡普里奥 ',
#     '评分': '9.3',
#     '评论': '诺兰给了我们一场无法盗取的梦.'
# }
# a4 = {
#     '电影名': '楚门的世界',
#     '导演': ['彼得·威尔', 'Peter Weir '],
#     '主演': ['金·凯瑞', 'Jim Carrey', '劳拉·琳妮'],
#     '评分': '9.3',
#     '评论': '如果再也不能见到你，祝你早安，午安，晚安。。'
# }
# a5 = {
#     '电影名': '大话西游之大圣娶亲',
#     '导演': ['刘镇伟', 'Jeffrey Lau'],
#     '主演': ['周星驰', 'Stephen Chow', '吴孟达', 'Man Tat Ng'],
#     '评分': '9.2',
#     '评论': '一生所爱。'
# }


# 1.
# 有字符串
# "key1:1|key2:2|key3:3|key4:5"
# 处理成字典
# {'key1': 1, 'key2': 2...}
old = "key1:1|key2:2|key3:3|key4:5"
center = old.replace('|', ' ').replace(':', ' ')
center = center.split(' ')
print(center, type(center))
new = {}
for i in range(0, len(center)):
    if i % 2 == 0:
        new[center[i]] = center[i + 1]
print(new)

# 2.
# 有列表a = [11, 77, 22, 33, 88, 44, 55, 77, 88, 70, 30, 99], 将所有大于60的值保存在字典的第一个key中, 将小于60的值保存在第二个key中:
# 格式: {'key1': 大于60的值列表, 'key2': 小于60的值列表}
# a = [11, 77, 22, 33, 88, 44, 55, 77, 88, 70, 30, 99]
# c = []
# b = []
# new = {}
# for i in a:
#     print(i)
#     if i > 60:
#         c.append(i)
#     if i < 60:
#         b.append(i)
# new['key1'] = c
# new['key2'] = b
# print(new)


# 3.
# 输出商品列表, 用户输入序号, 显示用户选中的商品
# 商品列表:
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],
#             ['wife', 10], ['wifi', 100000]]
# a.把商品列表变为:
# products = [{'name': 'iphone8', 'price': 6888}, {'name': 'MacPro', 'price': 14888}, {'name': '小米6', 'price': 2499},
#             {'name': 'Coffe', 'price': 31}....]
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],
# ['wife', 10], ['wifi', 100000]]
# new_products = []
# for i in products:
#     new = {}
#     new['name'] = i[0]
#     new['price'] = i[1]
#     new_products.append(new)
# print(new_products)

# b.在a的基础上, 页面显示: 序号 + 商品名称 + 商品价格:
#
# 1
# iphone8
# 6888
# 2
# MacPro
# 14888
# 3
# 小米6
# 2499
# ....
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],
# ['wife', 10], ['wifi', 100000]]
# new = {}
# new_products = []
# for i in range(0, len(products)):
#     new = {}
#     new['序号'] = i
#     new['name'] = products[i][0]
#     new['price'] = products[i][1]
#     new_products.append(new)
# print(new_products)


# c.用户输入商品的序号, 打印商品名称和价格
# xuhao = int(input('请输入商品序号:'))
# print(new_products[xuhao]['name'])
# print(new_products[xuhao]['price'])


# d.如果用户输入的商品序号有误(没有该商品), 提示输入有误, 并重新输入
#
# e.用户输入Q或者q, 退出程序
# while True:
#     userInput = input('请输入商品序号: ')
#     if userInput in 'Qq':
#         print('退出')
#         break
#     elif userInput.isdecimal():
#         if int(userInput) > 0 and int(userInput) <= len(products):
#             index = int(userInput) - 1
#             print('商品为: {},价格为: {}'.format(products[index]['name'], products[index]['price']))
#         else:
#             print('请输入正确的商品序号')
#     else:
#         print('输入有误!!!')




# 4.
# 电影投票, 由用户给每个电影打分, 最终显示每个电影的评分(用户输入分数);
# 电影列表: list = ['囧妈', '疯狂的外星人', '金瓶梅', '战狼', '哪吒传奇', '灵魂摆渡']
#
# 格式如下:
# 请给囧妈打分: 8
# 请给疯狂的外星人打分: 10
# ...
# ...
#
# 显示的结果:
# {'囧妈': 8, '疯狂的外星人': 10...}
# list = ['囧妈', '疯狂的外星人', '金瓶梅', '战狼', '哪吒传奇', '灵魂摆渡']
# new = {}
# for i in list:
#     j = input('请给%s打分:'%(i))
#     new[i] = j
# print(new)


# 5.
# 车牌区域计数:
# 所有的车牌号:
# cars = ['京A88888', '赣B12345', '沪C76543', '黑B33445', '京B22445', '沪A67854', '黑C67890']
#
# locals = {'沪': '上海', '黑': '黑龙江', '赣': '江西', '京': '北京'}
#
# 运行结果为:
# {'黑龙江': 2, '上海': 2, '北京': 2, '江西': 1}
# cars = ['京A88888', '赣B12345', '沪C76543', '黑B33445', '京B22445', '沪A67854', '黑C67890']
# locals = {'沪': '上海', '黑': '黑龙江', '赣': '江西', '京': '北京'}
# local = []
# diming = []
# new = {}
# for i in cars:
#     local.append(i[0])
# for j in local:
#     diming.append(locals[j])
# print(diming)
# for k in diming:
#     a = diming.count(k)
#     if k not in new:
#         new[k] = a
# print(new)


# 6.
# zhubo = {'卢本伟': 5000000, '冯提莫': 8888, 'UZI': 8000000000, 'mlxg': 1000000, 'letme': 88888888, '张琪格': 1000, '陈一发': 50000}
# a.计算主播的平均收益
# b.删除利益小于平均值的主播
# zhubo = {'卢本伟': 5000000, '冯提莫': 8888, 'UZI': 8000000000, 'mlxg': 1000000, 'letme': 88888888, '张琪格': 1000, '陈一发': 50000}
# sun = 0
# for i in zhubo.values():
#     sun += i
# average = sun / len(zhubo)
# print(len(zhubo))
# print(average)
# ming = []
# qian = []
# for j in zhubo.keys():
#     ming.append(j)
# print(ming)
# for h in zhubo.values():
#     qian.append(h)
# print(qian)
# for m in range(len(qian)):
#     if qian[m] < average:
#         del zhubo[ming[m]]
# print(zhubo)



# 7.
# 根据以下字典, 把数字的发音读出来
# dic = {
#     '-': 'fu',
#     '0': 'ling',
#     '1': 'yi',
#     '2': 'er',
#     '3': 'san',
#     '4': 'si',
#     '5': 'wu',
#     '6': 'liu',
#     '7': 'qi',
#     '8': 'ba',
#     '9': 'jiu',
#     '.': 'dian'
# }
# 运行:
# 请输入一个数: -328
# 发音为: fu
# san
# er
# ba
# dic = {
#     '-': 'fu',
#     '0': 'ling',
#     '1': 'yi',
#     '2': 'er',
#     '3': 'san',
#     '4': 'si',
#     '5': 'wu',
#     '6': 'liu',
#     '7': 'qi',
#     '8': 'ba',
#     '9': 'jiu',
#     '.': 'dian'
# }
# a = input('请输入一个数:')
# for i in a:
#     print(dic[i])



# 8.
# 思考题(仅做思考, 能实现最好!!!): 对于第7题, 假如要求读出:
# 请输入一个数: -328
# 发音为: fu
# san
# 百
# er
# 十
# ba
#
# 输入一个数: 1234
# 发音为: yi
# 千
# er
# 百
# san
# 十
# si
dic = {
	'-': 'fu',
	'0': 'ling',
	'1': 'yi',
	'2': 'er',
	'3': 'san',
	'4': 'si',
	'5': 'wu',
	'6': 'liu',
	'7': 'qi',
	'8': 'ba',
	'9': 'jiu',
	'.': 'dian'
}
# 构建发音列表
fayin = ['', '十', '百', '千', '万']
# 用户输入内容
userInput = '10201'

# 小数点部分的发音
xiaoshu = ''
# 判断是否为小数
if '.' in userInput:
	# 先找到.的位置
	index = userInput.find('.')
	# 切片取到.后面的内容
	float = userInput[index:]
	# 遍历.后边的内容
	for i in float:
		# dic[i]: 每个小数的发音
		xiaoshu += dic[i] + ' '
	# 取出整数部分赋值回去继续判断是否为负数
	userInput = userInput[:index]

# 假设有负数
fushu = ''
# 判断是否为负数
if '-' in userInput:
	# 取出负号后面的部分
	userInput = userInput[1:]
	# 做出负数和空格
	fushu = dic['-'] + ' '

# 整数位
result = ''
# 控制中间出现0的次数
flag = True
# i : 每个数字
for i in range(len(userInput)):
	# 发音的下标
	index = len(userInput) - 1 - i
	# 如果i是0则进入循环
	if userInput[i] == '0':
		# 如果连续是0则只输出一个零
		if flag == True:
			result += dic[userInput[i]] + ' '
			flag = False
	else:
		flag = True
		result += dic[userInput[i]] + ' ' + fayin[index] + ' '

# result: er 万 ling  # 截取到er 万
# 末尾有几个0
a = userInput
# print(a)
# 计数
count = 0
# 从后往前遍历,如果有0,则让count+1
a = a[::-1]
for i in a:
	if i == '0':
		count += 1
	else:# 0 是不连续kjh;
		break
# print(result)
if count > 0:
	# 查找发音在原来结果中的位置
	index = result.find(fayin[count])
	result = result[0:index + 1]

# 最终的结果
print(fushu + result + xiaoshu)


# 9.
# 将以下字符串变为字典的格式:
# https: // www.baidu.com / s?ie = utf - 8 & f = 8 & rsv_bp = 1 & rsv_idx = 1 & tn = baidu & wd = json
#
# a = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=json'
# index = a.rfind('?')
# a = a[index + 1:]
# # 先将&替换为=
# a = a.replace('&', '=')
# b = a.split('=')
# dic = {}
# # 遍历列表,按照下标遍历
# for i in range(0, len(b), 2):
#     print(b[i], b[i + 1])
#     dic[b[i]] = b[i + 1]
# print(dic)




#                                                                               - 名片管理系统(不考虑重复)
#
#                                                                               == == == == == == == == == == == == == == == == == == == == == == == == ==
#                                                                               名片管理系统 V0.01
#  1. 添加一个新的名片
#  2. 删除一个名片(先查找, 是否删除)
#  3. 修改一个名片(先查找, 是否修改)
#  4. 查询一个名片
#  5. 显示所有的名片(50条) [{}, {}, {}]
# 6.
# 退出系统
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# 每条数据都应该有: 姓名, QQ号, 微信号, 住址
#
#               - QQ(10
# 位随机数)
# - 微信(11
# 位随机数)
# - 纯数字
#
# - 默认的50条数据在程序运行的时候随机产生
# 请输入操作序号: 5
# aaa
# 8909
# weixin
# 北京
# bbb
# 9099
# weixin
# 上海
# - 增:
# - 请输入名字, qq, 微信, 住址
#          - 删
#          - 请输入要删除的名字
#          - 改(先查询, 再更新)
#          - 请输入要修改的名字: 请输入名字, qq, 微信, 住址
#
#                              - 查询某一个人的数据:
# - 请输入要查询的名字:
import random
# 提示文字
msg = '''==================================================
   名片管理系统 V0.01
 1. 添加一个新的名片
 2. 删除一个名片 (先查找,是否删除)
 3. 修改一个名片 (先查找,是否修改)
 4. 查询一个名片 
 5. 显示所有的名片 (50条) [{},{},{}]
 6. 退出系统
=================================================='''
print(msg)

# 姓
xing = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩","杨", "朱", "秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹", "喻", "柏", "水", "窦","章","云","苏","潘","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤"]
# 名
ming = ["涵清", "星舞", "秋枫", "晨月", "霁华", "烟霏", "殷云", "烟岚", "霏微", "夕佳", "思邈","紫琪","雅君","涵","鸿月","茜","雅洁","语彤", "梓璇","靖怡","倾哥","清浅","疏影","茗月","醉烟","月墨","云落","桂燕","子琴", "腊梅", "芬", "莉娅", "娟娣", "艳红", "棠莉" ,"悦驰" ,"婉婷", "嘉洁" ,"彩红", "媛雪", "美芳", "束芳", "淑琳", "若瑶","莉轩", "燕齐", "昕妍", "思思" ,"玉瑶" ,"子婧" ,"爱琴", "维娟", "思娜", "欢欢" ,"鸾瑶" ,"玲丽", "旦娅", "苏娟" ,"宝琳" ,"思念","羽洁", "秋艳", "建颖" ,"泓茹", "富霞", "倩成" ,"诗茹" ,"欣瑶", "曦秀", "婷丽", "莉娜" ,"东玲" ,"巧娜" ,"佳艳" ,"蓓莉" ,"纪颖"]
# 地址
addrs = ["北京", "上海", "广州", "深圳", "辽宁", "天津", "四川", "广西", "山东", "山西", "西安", "云南", "新疆", "呼和浩特", "包头", "赤峰", "鄂尔多斯","呼伦贝尔", "阿拉善盟", "济南", "青岛", "烟台", "威海", "潍坊", "德州", "滨州", "东营", "聊城", "菏泽", "临沂", "北京", "上海", "天津", "重庆","淄博", "泰安", "枣庄", "日照", "莱芜", "海阳", "平度", "莱阳", "石家庄", "沧州", "承德", "秦皇岛", "唐山", "保定", "廊坊", "邢台", "衡水"]
# 所有的名片 [{},{},{}]
allData = []
# 生成50条数据
for i in range(50):
    # 姓名
    name = random.choice(xing) + random.choice(ming)
    # qq
    qq = random.randint(1000000000,9999999999)
    # 微信
    wechat = random.randint(10000000000,99999999999)
    # 地址
    addr = random.choice(addrs)
    dic = {'姓名': name,'qq': qq,'微信': wechat,'地址': addr}
    allData.append(dic)
print(len(allData))

# 一个名片  {'姓名': xxx,'qq': xxxxx,'微信': xxxxx,'地址': xxxxc}


while True:
    userInput = input('请输入操作序号: ')
    if userInput == '1':
        # 添加名片
        name = input('请输入要添加的姓名:')
        qq = input('请输入要添加的qq:')
        wechat = input('请输入要添加的微信:')
        addr = input('请输入要添加的地址:')
        # 输入的数据拼凑成一个字典
        dic = {'姓名': name, 'qq': qq, '微信': wechat, '地址': addr}
        # 加入到总的数据里面
        allData.append(dic)
        print('添加成功!!!')
    if userInput == '2':
        # 删除
        name = input('请输入要删除的姓名: ')
        # 先查找该名字是否存在
        flag = True
        # 使用while循环进行删除,不会造成下标的移动
        i = 0
        while i < len(allData):
            person = allData[i]
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                # 是否删除
                isDelete = input('是否删除?y/n')
                if isDelete in 'yY是':
                    # 直接删除
                    allData.remove(person)
                    # 下标得-1
                    i -= 1
                print()
            i += 1
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('你要删除的人不存在')
    if userInput == '3':
        # 修改
        name = input('请输入要修改的姓名: ')
        # 先查找该名字是否存在
        flag = True
        # 使用while循环进行删除,不会造成下标的移动
        i = 0
        while i < len(allData):
            # 把列表中的元素赋值给了person
            person = allData[i]
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                print()
                # 是否删除
                isDelete = input('是否修改?y/n')
                if isDelete in 'yY是':
                    # 用户输入 (当用户输入为空的时候,显示原来的内容)
                    updateName = input('姓名: ') or person['姓名']
                    qq = input('qq: ') or person['qq']
                    wechat = input('微信: ') or person['微信']
                    addr = input('地址: ') or person['地址']
                    # 修改
                    allData[i]['姓名'] = updateName
                    allData[i]['qq'] = qq
                    allData[i]['微信'] = wechat
                    allData[i]['地址'] = addr
                    print('修改成功!!!')
            i += 1
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('你要修改的人不存在')
    if userInput == '4':
        # 查询
        name = input('请输入要查询的姓名: ')
        flag = True
        for person in allData:
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                print()
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('查无此人')
    if userInput == '5':
        # 显示所有
        for person in allData:
            # person: 每一张名片
            for data in person.values():
                print(data,end='\t')
            print()
            # print(person)
            # print(person['姓名'],end='\t')
            # print(person['qq'],end='\t')
            # print(person['微信'],end='\t\t')
            # print(person['地址'])
    if userInput == '6':
        print('退出操作!!!')
        break
