"""
Dijkstra to find min length from start point to other points
From: Chrome -> CS -> Data structure
"""

class Solution(object):
    def minLengthFromStartPoint(self, startPoint, graph):
        passed = [startPoint] # Start from startPoint
        noPassed = [x for x in range(len(graph)) if x != startPoint] # Add other points to noPassed
        dis = graph[startPoint] # Init distance from startPoint to other points

        while len(noPassed):
            """
            Find shortest distance from dis list
            Now index is the closest point regards current no passed points
            """
            index = noPassed[0]
            for i in noPassed:
                if dis[i] < dis[index]:
                    index = i
            passed.append(index) # The index is passed
            noPassed.remove(index) # The index is passed
            for i in noPassed:
                if dis[index] + graph[index][i] < dis[i]:
                    dis[i] = dis[index] + graph[index][i] # Update dis list if we find the distance is shorter

        return dis

solution = Solution()
startPoint = 0
inf = float("inf")
graph = [[0, 1, 12, inf, inf, inf],
          [inf, 0, 9, 3, inf, inf],
          [inf, inf, 0, inf, 5, inf],
          [inf, inf, 4, 0, 13, 15],
          [inf, inf, inf, inf, 0, 4],
          [inf, inf, inf, inf, inf, 0]]
dis = solution.minLengthFromStartPoint(startPoint, graph)
print(dis)