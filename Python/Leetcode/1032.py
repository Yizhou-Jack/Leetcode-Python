from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for s in word:
            node = node.children.setdefault(s, TrieNode())
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            reverseWord = word[::-1]
            self.trie.insert(reverseWord)
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream = [letter] + self.stream
        if len(self.stream) > 2000:
            self.stream.pop()
        currNode = self.trie.root
        for s in self.stream:
            if s in currNode.children:
                currNode = currNode.children[s]
                if currNode.isEnd:
                    return True
            else:
                break
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)