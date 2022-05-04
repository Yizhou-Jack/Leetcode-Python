class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isalpha() or c.isdigit() or c == "[":
                stack.append(c)
            else:
                repeatStr = ""
                while stack and stack[-1] != "[":
                    popChar = stack.pop()
                    repeatStr = popChar + repeatStr
                stack.pop()
                repeatTimes = 0
                times = 1
                while stack and stack[-1].isdigit():
                    popDigit = stack.pop()
                    repeatTimes += times*int(popDigit)
                    times *= 10
                stack.append(repeatTimes*repeatStr)
        return "".join(stack)