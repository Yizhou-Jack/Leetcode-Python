"""
Multiply Strings
"""

"""
n = len(num1)
m = len(num2)
resList -> len(resList) = (n+m)
nums[i]*nums[j] -> mul
mul stores in the resList[i+j+1]
mul may > 10 -> resList[i+j+1] = mul%10
"""

"""
on the top of my mind is that we can multiply the num string place by place
so we will have two nested for loop to iterate through
for each place pair, we can get the multiple result
we stores mul in the resList[i+j+1]
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        resList = [0]*(n+m)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                mul = int(num1[i])*int(num2[j])
                cul = resList[i+j+1]+mul
                resList[i+j+1] = cul%10
                resList[i+j] += cul//10
        res = ""
        flag = True
        for i in range(n+m):
            if resList[i] == 0 and flag:
                continue
            else:
                res += str(resList[i])
                flag = False
        return res if res != "" else "0"