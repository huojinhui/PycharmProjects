class Person:
    def __init__(self, name, age, height, sex):
        self.a = name
        self.b = age
        self.c = height
        self.d = sex
    def eat(self):
        print(('%s吃饭了' %(self.a)))
    def sleep(self):
        print(('%s睡觉了' %(self.a)))
class Student(Person):
    def __init__(self, name, age, height, sex, score):
        super().__init__(name, age, height, sex)
        self.score = score
    def text(self):
        print(('%s考试了' %(self.a)))
p1 = Student(name ='张三', sex='男', age=18, height=180, score=90)
p1.eat()
p1.sleep()
p1.text()
p2 = Student(name='lisi', sex='女', age=18, height=180, score=92)
p2.eat()
p2.sleep()
p2.text()
class Worker(Person):
    def __init__(self, name, sex, age, height, salary):
        super().__init__(name, sex, age, height)
        self.salary = salary
    def work(self):
        print('%s去上班' %(self.a))
p1 = Worker(name ='张三', sex='男', age=18, height=180, salary=5000)
p1.sleep()
p1.eat()
p1.work()