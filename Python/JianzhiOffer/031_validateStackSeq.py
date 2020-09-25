class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        length = len(popped)
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and i < length and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack