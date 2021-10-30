"""
Longest Duplicate Substring
Rabin Karp Algorithm
"""
from collections import defaultdict

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def RabinKarp(text, L):
            q = (1 << 31) - 1
            h, t, d = (1 << (8 * L - 8)) % q, 0, 256
            dic = defaultdict(list)
            for i in range(L):
                t = (d * t + ord(text[i])) % q
            dic[t].append(i - L + 1)
            for i in range(len(text) - L):
                t = (d * (t - ord(text[i]) * h) + ord(text[i + L])) % q
                for j in dic[t]:
                    if text[i + 1:i + L + 1] == text[j:j + L]:
                        return text[j:j + L]
                dic[t].append(i + 1)
            return None

        res = ""
        left, right = 1, len(s) - 1
        while left <= right:
            mid = (left + right) // 2
            dup = RabinKarp(s, mid)
            if dup:
                left = mid + 1
                res = dup
            else:
                right = mid - 1
        return res