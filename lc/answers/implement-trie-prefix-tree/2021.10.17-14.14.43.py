class Node:
    def __init__(self, char="*"):
        self._val = char
        self._children = {}
        self._is_end = False
    def has_child(self, char):
        return char in self._children
    def get_child(self, char):
        return self._children.get(char)
    def add_child(self, char):
        self._children[char] = Node(char)
    def mark_end(self):
        self._is_end = True
    def is_end(self):
        return self._is_end

class Trie:

    def __init__(self):
        self._parent_node = Node()   

    def insert(self, word: str) -> None:
        node = self._parent_node
        for char in word:
            if node.has_child(char):
                node = node.get_child(char)
            else:
                node.add_child(char)
                node = node.get_child(char)
        node.mark_end()

    def search(self, word: str) -> bool:
        node = self._parent_node
        for char in word:
            if node.has_child(char):
                node = node.get_child(char)
            else:
                return False
        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self._parent_node
        for char in prefix:
            if node.has_child(char):
                node = node.get_child(char)
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)