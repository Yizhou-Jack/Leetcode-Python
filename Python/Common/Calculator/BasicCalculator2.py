"""
Basic Calculator 2 (227)
Take "3+2*2" as an example.
s consists of integers and operators ('+', '-', '*', '/')
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack, num, op = [], 0, '+'
        s = s.replace(" ", "") + '+' # Add last num
        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)
            else:
                if op == '-':
                    stack.append(-num)
                elif op == '+':
                    stack.append(num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                num, op = 0, c
        return sum(stack)