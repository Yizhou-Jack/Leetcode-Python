nAndk = input().split(" ")
n = int(nAndk[0])
k = int(nAndk[1])

dict = {}
for i in range(n):
    line = input()
    value = dict[line]
    if value is None: value = 0
    value += 1
    dict[line] = value

from heapq import *
heap = []
for key, value in dict:
    heappush(heap, (value,key))
nlar = nlargest(k, heap, key=lambda x:x[0])
largeNum = nlar[0][0]
nlarSmall = nsmallest(1, nlar, key=lambda x:x[0])
smallNum = nlarSmall[0][0]
tmpList = []
for i in range(len(heap)):
    if heap[i][0] == smallNum:
        tmpList.append(heap[i][1])
tmpList.sort()
count = 0
for i in range(len(nlar)):
    if nlar[0] == largeNum:
        print(nlar[1])
