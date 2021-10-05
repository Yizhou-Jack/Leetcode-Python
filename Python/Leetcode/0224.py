"""
Basic Calculator
"""

class Solution(object):
    def calculate(self, s):
        res = 0
        sign = 1
        num = 0
        resStack = []
        signStack = []
        for c in s:
            if c.isdigit():
                num = 10*num+int(c)
            elif c == "+" or c == "-":
                res += num*sign
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                resStack.append(res)
                signStack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += num*sign
                num = 0
                res *= signStack.pop()
                res += resStack.pop()
        res += sign*num
        return res