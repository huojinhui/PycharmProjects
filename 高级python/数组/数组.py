class Arrary:
    def __init__(self, capacity):
        # 数组容量
        self.array = [None] * capacity
        # 有效容量
        self.size = 0

    def insert(self, index, element):
        if index < 0:
            raise IndexError("下标太小")
        if index > len(self.array):
            self.add_capacity()
        # 通过遍历将index位置后边的元素后移一位,然后插入
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def add_capacity(self):
        # 将旧数组的每一位添加到新数组,新数组为旧数组的2倍
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        # 将新数组改名
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='->')

    def remove(self, index):
        if index > 0 and index < self.size:
            for i in range(index, self.size):
                self.array[i] = self.array[i + 1]
            self.size -= 1


