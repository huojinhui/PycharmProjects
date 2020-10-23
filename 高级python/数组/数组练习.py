from typing import List


class Arrary:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index > len(self.array):
            self.add_capacity()
        if index < 0:
            raise IndexError("下标太小")
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def add_capacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in self.array:
            print(i)

    def remove(self, index):
        if self.size == len(self.array):
            self.add_capacity()
        if index > 0 and index < self.size:
            for i in range(index, self.size):
                self.array[i] = self.array[i + 1]
        else:
            raise IndexError("下标超限")
        self.size -= 1


a = Arrary(8)
a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.remove(2)
a.output()


def remove_repeat(num: List):
    fast = 1
    slow = 0
    while fast < len(num):
        if num[fast] == num[slow]:
            slow += 1
            num[slow] = num[fast]
            fast += 1
        else:
            fast += 1
    return slow + 1


def remove_zero(num: List):
    fast = 0
    slow = 0
    while fast < len(num):
        if num[fast] == 0:
            fast += 1
        else:
            num[slow] = num[fast]
            slow += 1
            fast += 1
    for i in range(slow, len(num)):
        num[i] = 0