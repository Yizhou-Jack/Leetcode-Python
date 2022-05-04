from collections import Counter
from collections import defaultdict

class Solution:
    def minDeletions1(self, s: str) -> int:
        nums = ["" for _ in range(10 ** 5 + 1)]
        letterNums = defaultdict(int)
        for letter in s:
            letterNums[letter] += 1
        res = 0
        for i in range(97, 123):
            letter = chr(i)
            letterNum = letterNums[letter]
            if letterNum == 0:
                continue
            else:
                if nums[letterNum] == "":
                    nums[letterNum] = letter
                else:
                    subRes = 0
                    for j in range(letterNum - 1, -1, -1):
                        subRes += 1
                        if nums[j] == "":
                            nums[j] = letter
                            break
                    res += subRes
        return res

    def minDeletions2(self, s: str) -> int:
        S = Counter(s)
        count = 0
        unique = set()
        for char, freq in S.items():
            while freq > 0 and freq in unique:
                freq -= 1
                count += 1
            unique.add(freq)
        return count