"""
First one:
idea is to find every pair of "ba" and calculate the pair remove time
we could have a stack to maintain the current cancellation status
(Example)
"""

"""
Second one:
aNum: occurrences of 'a' from right side
bNum: occurrences of 'b' from left side
Count the total occurrences of 'a' on the right and 'b' on the left for each index, find the min
"""

class Solution:
    def minimumDeletions1(self, s: str) -> int:
        res = 0
        stack = []
        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                stack.pop()
                res += 1
            else:
                stack.append(c)
        return res

    def minimumDeletions2(self, s: str) -> int:
        aNum = s.count('a')
        bNum = 0
        res = len(s)
        for c in s:
            if c == 'b':
                res = min(res, aNum+bNum)
                bNum += 1
            else:
                aNum -= 1
        return min(res, bNum)