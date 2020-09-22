def dfs(featureList, curDepth, n, combination):
    if curDepth == n:
        print("-".join(combination))
        return
    for item in featureList[curDepth]:
        combination.append(item)
        dfs(featureList, curDepth+1, n, combination)
        combination.pop(-1)

n = int(input())
featureList = []

for i in range(n):
    feature = input().split(" ")
    featureList.append(feature)

combination = [-1]*n

dfs(featureList, 0, n, [])

#--------------------------------------------------#
from itertools import product

n = int(input())
featureList = []

for i in range(n):
    feature = input().split(" ")
    featureList.append(feature)

for item in product(*featureList):
    print("-".join(item))