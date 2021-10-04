"""
Stone Game
"""
import collections
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        n = len(stones)
        for i in range(n):
            stones[i] = stones[i] % 3
        num0 = 0
        num1 = 0
        num2 = 0
        for i in range(n):
            if stones[i] == 0:
                num0 += 1
            elif stones[i] == 1:
                num1 += 1
            else:
                num2 += 1
        if num1 == 0 and num2 == 0: return False
        res1 = None
        if num1 > 0:
            tmpNum1 = num1 - 1 - min(num1 - 1, num2)
            tmpNum2 = num2 - min(num1 - 1, num2)
            aTurn = True if num0 % 2 == 1 else False
            if aTurn:
                if tmpNum1 == 0 and tmpNum2 == 0:
                    res1 = False
                else:
                    if tmpNum1 >= 2:
                        res1 = True
                    elif tmpNum2 >= 1:
                        res1 = False
                    else:
                        res1 = False
            else:
                if tmpNum1 == 0 and tmpNum2 == 0:
                    res1 = False
                else:
                    if tmpNum1 >= 2:
                        res1 = False
                    elif tmpNum2 >= 1:
                        res1 = True
                    else:
                        res1 = False
        res2 = None
        if num2 > 0:
            tmpNum1 = num1 - min(num1, num2 - 1)
            tmpNum2 = num2 - 1 - min(num1, num2 - 1)
            aTurn = True if num0 % 2 == 1 else False
            if aTurn:
                if tmpNum1 == 0 and tmpNum2 == 0:
                    res2 = False
                else:
                    if tmpNum1 >= 1:
                        res2 = False
                    elif tmpNum2 >= 2:
                        res2 = True
                    else:
                        res2 = False
            else:
                if tmpNum1 == 0 and tmpNum2 == 0:
                    res2 = False
                else:
                    if tmpNum1 >= 2:
                        res2 = True
                    elif tmpNum2 >= 1:
                        res2 = False
                    else:
                        res2 = True
        return res1 or res2

    def stoneGameIX2(self, stones):
        cnt = collections.Counter(a % 3 for a in stones)
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        return abs(cnt[1] - cnt[2]) > 2