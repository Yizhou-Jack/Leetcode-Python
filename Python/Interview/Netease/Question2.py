mAndn = input().split(" ")
m = int(mAndn[0])
n = int(mAndn[1])

potentialSet = set()
noConnectSet = set()
tree = [[-1]*2 for _ in range(m)]

for i in range(n):
    line = input().split(" ")
    parentIndex = int(line[0])-1
    sonIndex = int(line[2])-1
    if line[1] == 'left':
        tree[parentIndex][0] = sonIndex
    else:
        tree[parentIndex][1] = sonIndex

for i in range(len(tree)):
    if tree[i][0] != -1 and tree[i][1] != -1:
        potentialSet.add(i)
    elif tree[i][0] == -1 and tree[i][1] == -1:
        noConnectSet.add(i)

count = 0
for potIndex in potentialSet:
    if tree[potIndex][0] in noConnectSet and tree[potIndex][1] in noConnectSet:
        count += 1

print(count)