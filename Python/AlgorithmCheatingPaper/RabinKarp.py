from collections import defaultdict

"""
Rabin Karp [Find repeat string]
text: Complete string
L: Search string length
return: target length repeat string if it exists; None if it not exists

Time Complexity: O(n+m)
n: Complete string length
m: Search string length
"""
def RabinKarp(text, L):
    q = (1 << 31) - 1
    h, t, d = (1 << (8 * L - 8)) % q, 0, 256
    dic = defaultdict(list)
    for i in range(L):
        t = (d * t + ord(text[i])) % q
    dic[t].append(0)
    for i in range(len(text) - L):
        t = (d * (t - ord(text[i]) * h) + ord(text[i + L])) % q
        for j in dic[t]:
            if text[i + 1:i + L + 1] == text[j:j + L]:
                return text[j:j + L]
        dic[t].append(i + 1)
    return None

print(RabinKarp("banana", 3))