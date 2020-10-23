# 第一遍
# class node:
#     def __init__(self, date, next=None):
#         self.date = date
#         self.next = None
#
#     def __repr__(self):
#         return "node({})".format(self.date)
#
#
# class linklist:
#     def __init__(self):
#         self.head = None
#
#     def insert_head(self, date):
#         new_node = node(date)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#
#     def appent(self, date):
#         if self.head is None:
#             self.insert_head(node(date))
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = node(date)
#
#     def insert(self, i, date):
#         if self.head is None:
#             self.insert_head(date)
#         elif i == 1:
#             self.insert_head(date)
#         else:
#             temp = self.head
#             qian = temp
#             j = 1
#             while j < i:
#                 qian = temp
#                 temp = self.head.next
#                 j += 1
#             mode = node(date)
#             qian.next = mode
#             mode.next = temp
#
#     def __repr__(self):
#         current = self.head
#         string = ""
#         while current:
#             string += "{}-->".format(current)
#             current = current.next
#         return string + "END"
#
#     def linklist(self, object: list):
#         self.head = node(object[0])
#         php = self.head
#         for i in object[1:]:
#             php.next = node(i)
#             php = php.next
#
#     def delete_head(self):
#         temp = self.head
#         if self.head:
#             self.head = self.head.next
#             temp.next = None
#
#     def delect_tail(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None:
#                 self.head = None
#             else:
#                 while temp.next.next:
#                     temp = temp.next
#                 temp.next = None
#
#
# a = linklist()
# a.insert_head(2)
# a.appent(3)
# a.insert(2, 2)
# b = linklist()
# b.linklist(list(range(10)))
# b.delete_head()
# b.delect_tail()
# print(b)
# print(a)


# 第二遍

class node:
    def __init__(self, date, next=None):
        self.date = date
        self.next = None

    def __repr__(self):
        return "node({})".format(self.date)


class linklist:
    def __init__(self):
        self.head = None

    def insert_head(self, date):
        new_node = node(date)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def append(self, date):
        if self.head is None:
            self.insert_head(date)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node(date)

    def __repr__(self):
        current = self.head
        string = ""
        while current:
            string += "{}-->".format(current)
            current = current.next
        return string + "END"

    def insert(self, i, date):
        if self.head is None:
            self.insert_head(date)
        elif i == 1:
            self.insert_head(date)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev

    def __getitem__(self, index):
        current = self.head
        if current is None:
            raise ImportError("这个链表是空的")

    def reverse1(self):
        dummy = node(0)
        prev = self.head
        current = self.head.next
        while prev.next is None:
            dummy.next = current
            prev.next = prev.next.next
            current.next = prev







a = linklist()
a.insert_head(3)
print(a)
a.insert_head(4)
print(a)
a.reverse()
print(a)

