#Submission 2
class Trie:

    def __init__(self):
        self.s=set()

    def insert(self, word: str) -> None:
        self.s.add(word)

    def search(self, word: str) -> bool:
        for ele in self.s:
            if word==ele:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for ele in self.s:
            if ele.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#Submission 1
class Trie:

    def __init__(self):
        self.d={}

    def insert(self, word: str) -> None:
        self.d[word]=1

    def search(self, word: str) -> bool:
        for key in self.d:
            if word==key:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for key in self.d:
            if key.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)