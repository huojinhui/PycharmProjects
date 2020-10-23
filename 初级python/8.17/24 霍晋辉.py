# 1.Employee 类
# 	- 员工数 初始值为0, 每当新生成一个实例时,员工数加一
# 	- 员工: 姓名, 工资
# 	- 声明方法 displayCount: 打印出当前的总员工数 (类方法)
# 	- displaySalary : 打印每一个员工自己的名字和薪水.
# class Employee():
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def displayCount(self):
#         pass
#     def displaySalary(self):
#         print('name:{} salary:{}'.format(self.name, self.salary))
# p1 = Employee(name='张三', salary='8000')
# p1.displaySalary()
# p2 = Employee(name='张四', salary='7000')

# 2.设计一个人的类,有名字,体重;能吃,能跑;
# 	a.每次跑步会减肥0.5公斤
# 	b.每次吃东西体重会增加1公斤
# 	c.有个get_msg()方法,打印出名字,体重:
# 		我的名字叫: xxx 体重是:
# class Person:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#     def ran(self):
#         self.weight -= 0.5
#     def eat(self):
#         self.weight += 1
#     def get_msg(self):
#         print('我的名字叫{} 体重是{}'.format(self.name, self.weight ))
# p1 = Person('张三', 50)
# p1.ran()
# p1.eat()
# p1.eat()
# p1.get_msg()


# 3.定义一个圆类,有半径属性,其中有计算周长和面积的方法
# class Yuan:
#     def __init__(self, banjing):
#         self.banjing = banjing
#     def zhouchang(self):
#         chang = self.banjing * 2 * 3.14
#         print(chang)
#     def mianji(self):
#         ji = 3.14 * (self.banjing ** 2)
#         print(ji)
# a = Yuan(1)
# a.zhouchang()
# a.mianji()


# 4.补充代码实现:
# 	user_list = []
# 	while True:
# 		user_name = input('输入用户名: ')
# 		sex = input('输入性别: ')
# 		age = input('输入年龄: ')
# 		email = input('输入邮箱: ')
# 	a.把每个用户用对象表示
# 	b.当列表中添加3个对象以后,打印出3个对象的信息:
# 		我叫xxx,性别xx,今年xx岁了,我的邮箱是xxxx
# class Person:
#     def __init__(self, user_name, sex, age, email):
#         self.user_name = user_name
#         self.sex = sex
#         self.age = age
#         self.email = email
#     def add(self):
#         center = []
#         center.append(self.user_name)
#         center.append(self.sex)
#         center.append(self.age)
#         center.append(self.email)
#         user_list.append(center)
#         print(center)
#         count += 1
#         print(count)
#         if count == 3:
#             print(user_list)
# user_list = []
# p1 = Person('张三', '男', '18', 180)
# p1.add()
# p2 = Person('张si', '男', '18', 180)
# p2.add()
# p3 = Person('张si', '男', '20', 180)
# p3.add()


# 5.模拟英雄联盟中的游戏人物的类:
#  要求:
#   a.创建Role(角色)类
#   b.初始化方法中给对象封装 name,ad(攻击力),hp(血量)三个属性
#   c.创建一个attack方法,此方法是实例化的两个对象,互相攻击的功能
#    例:
#     实例化一个Role对象,盖伦,ad为10,hp为100
#     实例化另一个Role对象,亚索,ad为20,hp为80
#     attack方法要完成: '谁攻击谁,谁掉了多少血,还剩多少血的提示功能'
# class Role:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#     def attack1(self, b):
#         print('%s攻击了%s,%s掉了%s点血,还剩%s点血' %(self.name, b.name, b.name, self.ad, (b.hp - self.ad)))
# a = Role(name='盖伦', ad=10, hp=100)
# b = Role(name='亚索', ad=20, hp=80)
# a.attack1(b)
# b.attack1(a)


# 6.模拟英雄联盟中的游戏人物的类:
#  要求:
#   a.创建Role(角色)类,有name,ad(攻击力),hp(血量)三个属性
#   b.创建Arms(武器)类,有name,ad(攻击力),两个属性
#   c.创建一个attack方法,此方法是实例化的两个对象,互相用武器攻击的功能
#    例:
#     实例化一个Role对象,名字为盖伦,ad为10,hp为100
#     实例化另一Role个对象,名字为亚索,ad为20,hp为80
#     实例化一个Arms对象,名字为无尽之刃,ad为40
#
#     attack方法要完成: '谁拿什么武器攻击谁,谁掉了多少血,还剩多少血的提示功能'
# class Role():
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#     # 创建attack方法, 此方法是实例化的两个对象, 互相攻击的功能
#     def attack(self, role_attacked, arms_used):
#         role_attacked.hp -= (self.ad + arms_used.ad)
#         print('{}使用{}攻击{},{}掉了{}血,还剩{}血'.format(self.name, arms_used.name, role_attacked.name, role_attacked.name, self.ad, role_attacked.hp))
# class Arms():
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
# # 实例化两个Role对象,亚索,ad为20,hp为80
# gailun = Role(name='盖伦', ad=10, hp=100)
# yasuo = Role(name='亚索',ad=20, hp=80)
# # 实例化一个Arms对象,名字为无尽之刃,ad为40
# wujin = Arms(name='无尽之刃', ad=40)