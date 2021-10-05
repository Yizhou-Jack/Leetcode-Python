"""
Common solution for basic calculator
"""

class Solution:
    opPriority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1, '^': 2} # Priority of operations

    def calculate(self, s: str) -> int:
        s = "(" + s.replace(" ", "").replace("(-", "(0-") + ")" # Add "(" and ")"; replace negative number with "0-"
        n = len(s)
        opStack, numStack = [], [] # Operators stack & Numbers stack

        i = 0
        while i < n:
            c = s[i]
            i += 1
            if c.isdigit():
                num = int(c)
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                numStack.append(num)
            elif c == '(':
                opStack.append(c)
            elif c == ')':  # Calculate until see "("
                while opStack and opStack[-1] != '(':
                    self.calc(numStack, opStack)
                opStack.pop() # Pop "("
            else: # Other operations
                """
                Only calculate when operation in the stack has higher priority:
                Cannot calculate "+" if next operation is "*"; Can calculate "+" if next operation is "-"
                """
                while opStack and opStack[-1] != '(':
                    prevOp = opStack[-1]
                    if self.opPriority[prevOp] < self.opPriority[c]:
                        break
                    self.calc(numStack, opStack)
                opStack.append(c)

        return numStack[0]

    def calc(self, numStack: list, opStack: list) -> None:
        op, y, x = opStack.pop(), numStack.pop(), numStack.pop() if numStack else 0
        ans = 0
        if op == '+':
            ans = x + y
        elif op == '-':
            ans = x - y
        elif op == '*':
            ans = x * y
        elif op == '/':
            ans = x / y
        elif op == '%':
            ans = x % y
        elif op == '^':
            ans = pow(x, y)
        numStack.append(int(ans))
