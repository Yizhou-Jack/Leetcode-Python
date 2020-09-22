res = 0
numSet = set()
def backtrack(nStrList, subRes):
    global res
    if not nStrList:
        num = int("".join(subRes))
        if num not in numSet and num % m == 0:
            res += 1
            numSet.add(num)
        return
    for i in range(len(nStrList)):
        backtrack(nStrList[:i]+nStrList[i+1:], subRes+[nStrList[i]])
#get permute list
nAndm = input().split(" ")
nStrList = list(nAndm[0])
m = int(nAndm[1])
backtrack(nStrList, [])
print(res)

