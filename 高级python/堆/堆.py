class Heap:
    def __init__(self):
        self.data_list = []

    # 找到父节点
    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    # 交换俩节点
    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    # 插入节点
    def insert(self, data):
        # 将节点加入到尾部
        self.data_list.append(data)
        # 新加入节点的下标
        index = len(self.data_list) - 1
        # 找到父节点下标
        parent = self.get_parent_index(index)
        # 父节点不为空和父节点小于子节点的情况进行节点交换
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            # 更新变量index和parent
            index = parent
            parent = self.get_parent_index(parent)

    # 删除根节点
    def pop(self):
        # 删除根节点
        remove_data = self.data_list[0]
        # 将根结点提换为最后一个节点
        self.data_list[0] = self.data_list[-1]
        # 删除最后一个节点
        del self.data_list[-1]
        # 将堆进行排序使根最大
        self.heapify(0)
        return remove_data

    # 堆化(将堆进行排序,使根为最大)
    def heapify(self, index):
        max_index = index
        min_index = len(self.data_list) - 1
        while True:
            # 和左节点作比较
            if 2 * index + 1 <= min_index and self.data_list[index * 2 + 1] > self.data_list[max_index]:
                max_index = 2 * index + 1
            # 和右结点作比较
            if 2 * index + 1 <= min_index and self.data_list[index * 2 + 2] > self.data_list[max_index]:
                max_index = 2 * index + 2
            if max_index == index:
                break
            self.swap(max_index, index)
            index = max_index


a = Heap()
a.insert(6)
a.insert(8)
print(a.get_parent_index(1))
