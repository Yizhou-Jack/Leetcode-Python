"""
求一组points的凸包: 单调链解法
Time complexity: O(nlog(n))
Space complexity: O(n)
"""

from typing import List

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        # 检查当前点是否在最后两个点的逆时针方向上(小于0则为逆时针)
        def oriented(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        if len(points) < 4:
            return points

        points.sort()  # 按照x值正序排列
        hull = [points[0], points[1]]
        for i in range(2, len(points)):
            r = points[i]
            while len(hull) >= 2 and oriented(hull[-2], r, hull[-1]) < 0:
                hull.pop()
            hull.append(r)
        points = points[::-1]  # 按照x值逆序排列
        for i in range(1, len(points)):
            r = points[i]
            while len(hull) >= 2 and oriented(hull[-2], r, hull[-1]) < 0:
                hull.pop()
            hull.append(r)
        res = []
        for candidate in hull:
            if candidate not in res:
                res.append(candidate)
        return res

