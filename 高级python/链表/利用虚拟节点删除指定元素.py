class Node:
    def __init__(self, data):
        self.date = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def removeElement(self, value):
        dummy = Node(0)
        dummy.next = self.head
        current = dummy
        while current.next:
            if current.next.data == value:
                temp = current.next
                current.next = current.next.next
                temp.next = None
            else:
                current = current.next
        return dummy.next


