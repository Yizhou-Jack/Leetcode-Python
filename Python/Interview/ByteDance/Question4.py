n, m, s = map(int, input().split())
arr = list(map(int, input().split()))

import math
def dfs(arr, i, magicNum, currSum):
    global res
    if currSum == s:
        res += 1
        return
    if i == len(arr) or currSum > s: return
    dfs(arr, i+1, magicNum, currSum+arr[i])
    dfs(arr, i+1, magicNum, currSum)
    if magicNum > 0:
        dfs(arr, i+1, magicNum-1, currSum+math.factorial(arr[i]))

res = 0
dfs(arr, 0, m, 0)
print(res)

