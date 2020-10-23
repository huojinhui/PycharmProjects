class node:
    def __init__(self, date, next=None):
        self.date = date
        self.next = None

    def __repr__(self):
        return "node({})".format(self.date)


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 按下表找出元素
    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    # 倒数第k个节点
    def rget(self, k):
        current = self.head
        for i in range(self.size - k):
            current = current.next
        return current

    # 插入
    def insert(self, index, date):
        new_node = node(date)
        if index < 0 or index > self.size:
            raise IndexError("不符合要求")
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    # 显示
    def __repr__(self):
        current = self.head
        string = ""
        while current:
            string += f"{current} -- >"
            current = current.next
        return string + "end"

    # 删除
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("不符合规范")
        elif index == 0:
            remove_node = self.head
            self.head = self.head.next
            self.head.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return remove_node

    def huan(self):
        self.tail.next = self.head.next
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast.next.next == slow.next:
                return "是"
            else:
                return "否"




a = linklist()
a.insert(0, 1)
a.insert(0, 2)
a.insert(0, 3)
b = a.rget(2)

print(a.huan())
print(b)
# print(a)
