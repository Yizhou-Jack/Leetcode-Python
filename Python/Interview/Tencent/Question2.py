nAndm = input().split(" ")
n = int(nAndm[0])
m = int(nAndm[1])

groupList = []
for i in range(m):
    peopleIds = input().split(" ")
    peopleNum = int(peopleIds[0])
    group = []
    for j in range(peopleNum):
        group.append(int(peopleIds[j+1]))
    groupList.append(group)

queue = []
queue.append(0)
knownList = set()
knownPeople = set()
while len(queue) > 0:
    element = queue.pop(0)
    knownPeople.add(element)
    for i in range(len(groupList)):
        if i in knownList:
            continue
        if element in groupList[i]:
            knownList.add(i)
            for j in range(len(groupList[i])):
                if groupList[i][j] in knownPeople:
                    continue
                knownPeople.add(groupList[i][j])
                queue.append(groupList[i][j])

print(len(knownPeople))


