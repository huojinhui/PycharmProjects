# import random
# print(random.randint(0,2))


while True:
    import random
    userInput = int(input('用户输入石头(0)  剪刀(1)  布(2): '))
    computerInput = random.randint(0, 2)
    if userInput == 0:
        user = '石头'
    elif userInput == 1:
        user = '剪刀'
    else:
        user = '布'
    if computerInput == 0:
        computer = '石头'
    elif computerInput == 1:
        computer = '剪刀'
    else:
        computer = '布'
    result = userInput - computerInput
    if result == - 1 or result == 2:
        print('用户胜,用户出的为%s,电脑出的为%s' % (user, computer))
        exit()

    elif result == 0:
        print('平局,用户出的为%s,电脑出的为%s' % (user, computer))
    else:
        print('电脑胜,电脑出的为%s,用户出的为%s' % (computer, user))
print('游戏结束')
