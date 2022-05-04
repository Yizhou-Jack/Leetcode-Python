from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        div = n//2
        remain = n%2
        res = [] if remain == 0 else [0]
        for i in range(1, div+1):
            res.append(i)
            res.append(-i)
        return res