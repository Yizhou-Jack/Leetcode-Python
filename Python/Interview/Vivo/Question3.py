from collections import deque

inputStrList = input().split(",")
fileNum = len(inputStrList)
inDegrees = [0 for _ in range(fileNum)]
neiborTable = [set() for _ in range(fileNum)]

for i in range(fileNum):
    start = int(inputStrList[i])
    if start == -1: continue
    end = i
    inDegrees[end] += 1
    neiborTable[start].add(end)

res = []
queue = deque([])
for i in range(fileNum):
    if inDegrees[i] == 0:
        queue.append(i)

while queue:
    element = queue.popleft()
    res.append(str(element))
    for successor in neiborTable[element]:
        inDegrees[successor] -= 1
        if inDegrees[successor] == 0:
            queue.append(successor)

print(",".join(res))

