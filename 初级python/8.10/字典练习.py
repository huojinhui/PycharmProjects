message = []
for i in range(1, 4):
    input('请输入第{}个人的信息:'.format(i))
    name = input('姓名:')
    age = input('年龄:')
    xingbie = input('性别:')
    jiguan = input('籍贯:')
    a = {'name': name, 'age': age, 'xingbie': xingbie, 'jiguan': jiguan}
    message.append(a)
for i in range(1, 4):
    print(message[i - 1]['name'], message[i - 1]['age'], message[i - 1]['xingbie'], message[i - 1]['jiguan'])

