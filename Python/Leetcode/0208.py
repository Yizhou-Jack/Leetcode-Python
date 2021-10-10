"""
Implement Trie (Prefix Tree)
"""

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
          if w not in t:
            t[w] = {}
          t = t[w]
        t["end"] = True

    def search(self, word: str) -> bool:
        t = self.trie
        for w in word:
          if w in t:
            t = t[w]
          else:
            return False
        return "end" in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for w in prefix:
          if w in t:
            t = t[w]
          else:
            return False
        return True