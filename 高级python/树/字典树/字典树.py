a = {
    "s": {
        "m": {
            "0": {
                "e": {
                    "t": {
                        "h": {
                            "i": {
                                "n": {
                                    "j": {}
                                }
                            }
                        },
                        "i": {
                            "m": {
                                "e": {}
                            }
                        }
                    },
                    "w": {
                        "h": {
                            "e": {
                                "r": {
                                    "e": {}
                                }
                            }
                        }
                    },
                }
            }
        }
    }
}


class Trie_node:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = Trie_node()
            node = node.data[char]
        node.is_word = True

    def __repr__(self):
        return str(self.root)

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if node is None:
                return False
        return node.is_word

    def startwith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if node is None:
                return False
        return True


b = Trie()
b.insert("something")
print(b.search("something"))
print(b.startwith("so"))
print(b)