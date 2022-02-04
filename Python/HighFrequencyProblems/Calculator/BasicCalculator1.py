"""
Basic Calculator 1 (224)
Take "(1+(4+5+2)-3)+(6+8)" as an example.
s consists of digits, '+', '-', '(', ')', and ' '
"""

class Solution(object):
    def calculate(self, s):
        res = 0
        sign = 1
        num = 0
        resStack = [] # Save res before "(", here is "1" (for second "(")
        signStack = [] # Save sign before "(", here is 1 == "+" (for second "(")
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c == '+' or c == '-':
                res += num*sign # Add num before sign to res (here is 1 for the first "+")
                num = 0 # Reset num
                sign = 1 if c == '+' else -1
            elif c == '(':
                resStack.append(res) # Save res before "(",
                signStack.append(sign) # Save sign before "("
                res = 0 # Reset res to calculate subRes inside "()"
                sign = 1
            elif c == ')':
                res += num*sign # Add num*sign before ")" into subRes, here is "2" (for first ")")
                res *= signStack.pop() # Get sign for subRes, here is "1" for first "()"
                res += resStack.pop() # Add subRes into res
                num = 0
        res += num*sign # Add last num into res
        return res