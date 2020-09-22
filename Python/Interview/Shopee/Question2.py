nStrList = list(input())
nList = []
for i in range(len(nStrList)):
    nList.append(int(nStrList[i]))

i = 0
index = -1
while i < len(nList):
    if i+1 < len(nList) and nList[i] > nList[i+1]:
        index = i
    i += 1
if index == -1:
    print(0)
else:
    preList = nList[0:index]
    forList = nList[index+1:]
    diff = 10
    index2 = -1
    for i in range(len(forList)):
        if nList[index]>forList[i] and nList[index]-forList[i]<diff:
            index2 = i
            diff = nList[index]-forList[i]
    middle = [forList[index2]]
    forList[index2] = nList[index]
    forList.sort()
    forList.reverse()
    res = preList+middle+forList
    resList = []
    for i in range(len(res)):
        resList.append(str(res[i]))
    print("".join(resList))