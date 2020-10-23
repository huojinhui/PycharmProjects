# # 利用数组建栈
# class Stark:
#     def __init__(self):
#         self.stark = []
#         self.size = 0
#
#     def push(self, data):
#         self.stark.append(data)
#         self.size += 1
#
#     def pop(self):
#         if self.stark:
#             temp = self.stark.pop()
#             self.size -= 1
#         else:
#             raise Exception("空")
#         return temp
#
#     def __repr__(self):
#         return f"{self.stark}"
#
#     def peek(self):
#         if self.stark:
#             return self.stark[-1]
#
#     def is_empty(self):
#         return not bool(self.stark)
#
#     def sizeof(self):
#         return self.size


# a = Stark()
# a.push(2)
# print(a.sizeof())

# 利用链表建一个栈
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.top = None
        self.size = 0

    def pull(self, data):
        new = Node(data)
        if self.top is None:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1
    
    def pop(self, data):
        if self.top is None:
            raise IndexError("列表为空")
        else:
            current = self.top
            self.top = current.next
            current.next = None
        self.size -= 1




