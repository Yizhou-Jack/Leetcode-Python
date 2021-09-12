"""
Basic Calculator
"""

class Solution(object):
    def calculate(self, s):
        res = 0
        sign = 1
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = 10*num+int(c)
            elif c == "+" or c == "-":
                res += num*sign
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += num*sign
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign*num
        return res