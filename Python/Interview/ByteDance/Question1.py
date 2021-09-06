n, m = map(int, input().split())

dict = {}
for i in range(n):
    id, point = map(int, input().split())
    sumPoint = 0 if dict.get(id, None) is None else dict.get(id)
    sumPoint += point
    dict[id] = sumPoint

import heapq
heap = []
for id, point in dict.items():
    if len(heap) < m:
        heapq.heappush(heap, [point, id])
    else:
        small = heap[0]
        if point > small[0] or (point == small[0] and id < small[1]):
            heapq.heapreplace(heap, [point, id])

nLarge = heapq.nlargest(m, heap)
res = []
for i in range(len(nLarge)):
    res.append(str(nLarge[i][1]))
print(" ".join(res))

