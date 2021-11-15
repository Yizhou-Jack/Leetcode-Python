"""
Iterator for Combination
"""

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combines = []
        def helper(index, track):
            if len(track) == combinationLength:
                self.combines.append("".join(track))
                return
            for i in range(index, len(characters)):
                track.append(characters[i])
                helper(i+1, track)
                track.pop()
        helper(0, [])
        self.k = 0

    def next(self) -> str:
        temp = self.combines[self.k]
        self.k += 1
        return temp

    def hasNext(self) -> bool:
        return True if self.k < len(self.combines) else False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()