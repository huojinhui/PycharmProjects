# 节点
class node:
    def __init__(self, date, next=None):
        self.date = date
        self.next = None

    def __repr__(self):
        return "node({})".format(self.date)


# 链表
class linkedlist:

    def __init__(self):
        self.head = None

    # 头部插入
    def insert_date(self, date):
        new_node = node(date)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    # 尾部插入
    def append(self, date):
        if self.head is None:
            self.insert_date(date)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node(date)

    # 显示
    def __repr__(self):
        current = self.head
        string = ""
        while current:
            # string += "{} -->".format(current)
            string += f"{current} -->"
            current = current.next
        return string + "END"

    # 指定位置插入
    def insert(self, i, date):
        if self.head is None:
            self.insert_date(date)
        elif i == 1:
            self.insert_date(date)
        else:
            temp = self.head
            pre = temp
            j = 1
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            b = node(date)
            pre.next = b
            b.next = temp

    # 插入列表
    def linkedlist(self, object: list):
        self.head = node(object[0])
        php = self.head
        for i in object[1:]:
            php.next = node(i)
            php = php.next  # 换掉头部

    # 删掉头
    def delect_head(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None

    # 删掉尾部
    def delect_tail(self):
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    # 反转链表
    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev

    # 索引
    def __getitem__(self, index):
        current = self.head
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(1, index):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        return current

    def get(self, index):
        return self.__getitem__(index)

    # 更改值
    def __setitem__(self, index, date):
        current = self.head
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(1, index):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        current.date = date

a = linkedlist()
a.insert_date(1)
a.insert_date(2)
a.append(5)
c = linkedlist()
c.linkedlist(list(range(9)))
c.delect_head()
c.delect_tail()
c.reverse()
print(c.get(3))

print(a)
print(c)
