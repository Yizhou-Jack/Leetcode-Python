from cmath import inf
from collections import defaultdict
from queue import PriorityQueue as PQ
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        connect = defaultdict(dict)
        print(connect)
        destinations = set()
        for start, end, price in flights:
            destinations.add(end)
            connect[start][end] = price
        print(connect)
        if dst not in destinations:
            return -1
        cheapest = inf
        q = PQ()
        q.put((0, src, 0))
        while not q.empty():
            price, start, t = q.get()
            if price >= cheapest:
                break
            if start == dst:
                cheapest = min(cheapest, price)
                continue
            if t <= k:
                for nxt in connect[start]:
                    q.put((price + connect[start][nxt], nxt, t + 1))
        return cheapest if cheapest != inf else -1

n = 13
flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
src = 10
dst = 1
k = 10
solution = Solution()
res = solution.findCheapestPrice(n, flights, src, dst, k)
print(res)

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        memo = [0]*n
        for i in range(n):
            if memo[i] == 1:
                continue
            for j in range(n):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    memo[i] = 1
                    break
                if properties[i][0] > properties[j][0] and properties[i][1] > properties[j][1]:
                    memo[j] = 1
        res = 0
        for i in range(n):
            if memo[i] == 1:
                res += 1
        return res

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        attackOrderPros = sorted(properties)
        order = 0
        attackOrderPros[0].append(0)
        for i in range(1,n):
            if attackOrderPros[i][0] == attackOrderPros[i-1][0]:
                attackOrderPros[i].append(order)
            else:
                order += 1
                attackOrderPros[i].append(order)
        defenseOrderPros = sorted(attackOrderPros, key=lambda x:x[1])
        print(attackOrderPros)
        print(defenseOrderPros)
        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if defenseOrderPros[i][2] < defenseOrderPros[j][2] and defenseOrderPros[i][1] != defenseOrderPros[j][1]:
                    res += 1
                    break
        return res