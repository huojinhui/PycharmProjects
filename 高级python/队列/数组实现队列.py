class Queue:
    def __init__(self):
        self.entries = []
        self.size = 0

    def __repr__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def enqueue(self, item):
        self.entries.append(item)
        self.size += 1

    def dequeue(self):
        item = self.entries[0]
        self.entries = self.entries[1:]
        self.size -= 1
        return item

    def get(self, index):
        if index < 0 or index > self.size:
            raise IndexError("下标超出范围")
        item = self.entries[index:index+1]
        return item

    def long(self):
        return self.size


a = Queue()
a.enqueue(1)
a.enqueue(1)
a.enqueue(1)
a.enqueue(4)
a.dequeue()
print(a.long())
print(a.get(2))
print(a)
