class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Queue:
    def __init__(self):
        self.font = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.font is None:
            self.font = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.font is None:
            raise IndexError("空队列")
        else:
            remove_node = self.font
            self.font = self.font.next
            remove_node.next = None
        self.size -= 1
        return remove_node

    def __repr__(self):
        current = self.font
        str = ""
        while current:
            str += f"{current}" + "-->"
            current = current.next
        return str + "end"


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
