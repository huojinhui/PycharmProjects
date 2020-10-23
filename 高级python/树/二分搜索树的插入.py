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

    def search(self, data):
        if self.is_empty():
            raise IndexError("空树")
        else:
            node = self.root
            while node and node.data != data:
                if data < node.data:
                    node = node.left
                elif data > node.data:
                    node = node.right
            print(node)
            return node

    # 重新分配
    def __reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self, value):
        node = self.search(value)
        if node:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node, None)
            elif node.left is None:
                self.__reassign_nodes(node, node.right)
            elif node.right is None:
                self.__reassign_nodes(node, node.left)
            else:
                temp = self.get_max(node.left)
                self.remove(temp.data)
                node.data = temp.data

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def is_right(self, node):
        return node == node.parent.right


a = Tree()
print(a.insert(51, 10, 3, 4, 50, 6, 7, 8, 9))
a.remove(51)
print(a)