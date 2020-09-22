nAndm = input().split(" ")
n = int(nAndm[0])
m = int(nAndm[1])
numsStrList = input().split(" ")
nums = [int(i) for i in numsStrList]
nums.sort()
modNum = 10**9+7

oddList = [0 for _ in range(n)]
evenList = [0 for _ in range(n)]
oddList[0] = 1 if nums[0] % 2 == 1 else 0
evenList[0] = 1 if nums[0] % 2 == 0 else 0
for i in range(1,n):
    if nums[i] % 2 == 1:
        oddList[i] = oddList[i-1]+1
        evenList[i] = evenList[i-1]
    else:
        oddList[i] = oddList[i-1]
        evenList[i] = evenList[i-1]+1
indexDict = {}
for i in range(n):
    indexDict[nums[i]] = i

for i in range(m):
    line = input().split(" ")
    flag = int(line[0])
    startIndex = indexDict[int(line[1])]
    endIndex = indexDict[int(line[2])]
    oddCount = oddList[endIndex]-oddList[startIndex]+1
    evenCount = evenList[endIndex]-evenList[startIndex]+1
    oddComRes = 2**oddCount-1
    if flag == 1:
        print(oddComRes % modNum)
    else:
        evenComRes = 2**evenCount-1
        comRes = oddComRes*evenComRes
        print((evenComRes+comRes)%modNum)

