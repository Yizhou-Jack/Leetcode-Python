"""
Score of Parentheses
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for val in s:
            if val == "(":
                stack.append(res)
                res = 0
            else:
                res = stack.pop() + max(1, res*2)
        return res