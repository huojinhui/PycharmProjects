# 数组实现栈
class Stark:
    def __init__(self):
        self.stark = []
        self.size = 0

    def push(self, data):
        self.stark.append(data)
        self.size += 1

    def pop(self):
        self.stark.pop()
        self.size -= 1


# 链表实现
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stark_list:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            self.size += 1
        else:
            new = Node(data)
            new.next = self.top
            self.top = new
            self.size += 1

    def pop(self):
        remove = self.top
        remove.next = self.top
        self.top.next = None
        self.size -= 1
        return remove


