"""
Min Stack
"""

class MinStack:

    def __init__(self):
        self.minStack = []
        self.aStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.aStack or self.aStack[-1] >= val:
            self.aStack.append(val)

    def pop(self) -> None:
        popVal = self.minStack.pop()
        if self.aStack and self.aStack[-1] == popVal:
            self.aStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.aStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()