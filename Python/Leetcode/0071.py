"""
Simplify Path
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathList = path.split("/")
        for element in pathList:
            if element == "..":
                if stack:
                    stack.pop()
            elif element == "." or element == '':
                continue
            else:
                stack.append(element)
        stack = [""] + stack
        return "/".join(stack) if len(stack) > 1 else "/"