# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)
import random
hong = list(range(1, 34))
blue = list(range(1, 17))
call = []
call.extend(random.sample(hong, 6))
call.extend(random.sample(blue, 1))
print(call)
# 5. 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
n = int(input('请输入一个数:'))
a = list(range(1, n + 1))
print(random.sample(a, n))