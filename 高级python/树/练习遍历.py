from pprint import pformat


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data): (self.left, self.right)}, indent=1)


class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def __insert(self, data):
        new = Node(data, None)
        if self.is_empty():
            self.root = new
        else:
            parent_node = self.root
            while True:
                if new.data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new
                        break
                    else:
                        parent_node = parent_node.left
                elif new.data > parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = new
                        break
                    else:
                        parent_node = parent_node.right
            # 维护父属性
            new.parent = parent_node

    def insert(self, *data):
        for i in data:
            self.__insert(i)
        return self

    def __str__(self):
        return str(self.root)

    



