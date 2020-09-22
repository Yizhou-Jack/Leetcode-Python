nAndk = input().split(" ")
n = int(nAndk[0])
k = int(nAndk[1])

suList = [set() for _ in range(n+1)]
for i in range(1, n+1):
    sus = input().split(" ")
    su1 = int(sus[0])
    su2 = int(sus[1])
    suList[su1].add(i)
    suList[su2].add(i)

res = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        unionRes = suList[i] | suList[j]
        if len(unionRes) >= k:
            res += 1
print(res)