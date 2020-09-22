class CQueue:

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def appendTail(self, value):
        self.stackIn.append(value)

    def deleteHead(self):
        if not self.stackOut:
            if not self.stackIn:
                return -1
            else:
                while self.stackIn: #Pour stackIn elements into stackOut when no element in the stackOut
                    element = self.stackIn.pop()
                    self.stackOut.append(element)
        return self.stackOut.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()