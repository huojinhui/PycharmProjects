class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent_index = self.get_parent(index)
        while parent_index is not None and self.data_list[parent_index] < self.data_list[index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = self.get_parent(parent_index)

    def pop(self):
        remove = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify()
        return remove

    def heapify(self):
        max_index = 0
        min_index = len(self.data_list) - 1
        while True:
            if max_index <= min_index and self.data_list[2 * max_index + 1] > self.data_list[max_index]:
                max_index = 2 * max_index + 1
            if max_index <= min_index and self.data_list[2 * max_index + 2] > self.data_list[max_index]:
                max_index = 2 * max_index + 2
            if max_index == 0:
                break
            self.swap(0, max_index)

    def up_heapify(self):
        last_index = len(self.data_list) - 1
        while True:
            parent_index = self.get_parent(last_index)
            if parent_index:
                if self.data_list[parent_index] < self.data_list[last_index]:
                    self.data_list[parent_index], self.data_list[last_index] = self.data_list[last_index], self.data_list[parent_index]
                    last_index = parent_index
                else:
                    break
            else:
                break

    def ouoput(self):
        for i in self.data_list:
            print(i)

    def abc(self, data):
        self.data_list.append(data)


a = Heap()
a.insert(12)
a.insert(9)
a.insert(10)
a.insert(10)
a.abc(20)
print(a.data_list)
a.up_heapify()

print(a.data_list)



