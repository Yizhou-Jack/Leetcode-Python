"""
Longest Diverse String
"""

"""
input -> int:a, int:b, int:c
output -> string:res

assume: a = 1, b = 1, c = 7
res = []
compare a,b,c
find c is largest one
res.append(c)
now: res[-1] = c, res[-2] is invalid
compare a,b,c
find c is largest one
res.append(c)
now: res[-1] = c, res[-2] = c
    if find a is second largest one and the value > 0
        res.append(a)
    else: (value = 0) -> (a:0, b:0) -> we only have c now but we can not append c into this list
        break
return res
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        We need to store abc into a list since we are going to get the largest value or second largest value
        in these three values, so we may do sort for this list
        trick: write a, b, c first
        track: take 7 1 1 as an example
        """
        abcList = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = []
        while True:
            abcList.sort()
            i = 1 if len(res) >= 2 and res[-2] == res[-1] == abcList[2][1] else 2
            if abcList[i][0] > 0:
                res.append(abcList[i][1])
                abcList[i][0] -= 1
            else:
                break
        return "".join(res)