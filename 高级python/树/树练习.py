class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.data}"


class Tree:
    def __init__(self):
        self.root = None

    def add_tree(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        current = [self.root]
        while True:
            temp = current.pop(0)
            if temp.left is None:
                temp.left = new_node
                return
            elif temp.right is None:
                temp.right = new_node
                return
            else:
                current.append(temp.right)
                current.append(temp.left)


a = Tree()
a.add_tree(2)
a.add_tree(3)
a.add_tree(4)

