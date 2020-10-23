from pprint import pformat


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)


class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __insert(self, data):
        new_node = Node(data, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *data):
        for i in data:
            self.__insert(i)
        return self

    def __str__(self):
        return str(self.root)

    # 前序遍历
    def preOrderTraverse(self, node):
        if not node:
            return None
        print(node.data)
        self.preOrderTraverse(node.left)
        self.preOrderTraverse(node.right)

    def preOrderTraverse2(self, node):
        stark = [node]
        while len(stark) > 0:
            print(node.data, end=" ")
            if node.right:
                stark.append(node.right)
            if node.left:
                stark.append(node.left)
            node = stark.pop()

    # 中序遍历
    def midOrderTraverse(self, node):
        if not node:
            return None
        self.preOrderTraverse(node.left)
        print(node.data)
        self.preOrderTraverse(node.right)

    def midOrderTraverse2(self, node):
        stark = []
        while node or len(stark) > 0:
            while node:
                stark.append(node)
                node = node.left
            if len(stark) > 0:
                node = stark.pop()
                print(node.data)
                node = node.right

    # 后序遍历
    def tailOrderTraverse(self, node):
        if not node:
            return None
        self.preOrderTraverse(node.left)
        self.preOrderTraverse(node.right)
        print(node.data)

    def tailOrderTraverse2(self, node):
        if node is None:
            return False
        stark1 = []
        stark2 = []
        stark1.append(node)
        while stark1:
            node = stark1.pop()
            if node.left:
                stark1.append(node.left)
            if node.right:
                stark1.append(node.right)
            stark2.append(node)

    # 层序遍历
    def Sequence_traversal(self):
        if self.root is None:
            raise IndexError("空树")
        else:
            a = []
            a.append(self.root)
            while a is not None:
                node = a.pop(0)
                print(node.data)
                if node.left:
                    a.append(node.left)
                if node.right:
                    a.append(node.right)


a = Tree()
print(a.insert(51, 10, 3, 4, 50, 6, 7, 8, 9))
a.preOrderTraverse2(a.root)
a.midOrderTraverse(a.root)
a.tailOrderTraverse(a.root)
