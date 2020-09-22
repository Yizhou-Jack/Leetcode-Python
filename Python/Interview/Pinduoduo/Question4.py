nAndm = input().split(" ")
n = int(nAndm[0])
m = int(nAndm[1])
mList = []
for i in range(m):
    tmp = int(input())
    mList.append(tmp)

nums = [i+1 for i in range(n)]
boolList = [0]*n
for i in range(len(mList)):
    m = mList[i]
    for j in range(0, len(nums)):
        if boolList[j] == 1:
            continue
        else:
            if nums[j]%m == 0:
                boolList[j] = 1

res = 0
for i in range(len(boolList)):
    if boolList[i] == 1:
        res += 1

print(res)