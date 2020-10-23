class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.data})"


class Tree:
    def __init__(self):
        self.root = None

    # 增加元素
    def add_tree(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        temp = [self.root]
        while True:
            # 更新current的值
            current = temp.pop(0)
            if current.left is None:
                current.left = new
                return
            elif current.right is None:
                current.right = new
                return
            else:
                temp.append(current.left)
                temp.append(current.right)

    # 找到父结点
    def get_tree(self, data):
        if self.root == data:
            return None
        temp = [self.root]
        while temp:
            current = temp.pop(0)
            if current.left.data == data:
                return current
            if current.right.data == data:
                return current
            if current.left:
                temp.append(current.left)
            if current.right:
                temp.append(current.right)
            return None

    



a = Tree()
a.add_tree(2)
a.add_tree(3)
print(a.root)
