from typing import Optional


class Node:
    def __init__(self, data):
        self.date = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError("下标超过范围")
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

    def remove(self, index):
        if self.size == 0:
            raise ImportError("列表是空的")
        if index < 0 or index >= self.size:
            raise ImportError("下标超出范围")
        elif index == 0:
            remove_node = self.head
            self.head = self.head.next
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return remove_node


def is_circle(head: Node):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def detectcirclepoint(head: Optional[Node] = None):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    node1 = Node(1)
