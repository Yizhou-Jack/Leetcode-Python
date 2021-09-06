a, b = map(int, input().split())
n = a if b == 2 else b

dp = [0 for _ in range(n)]
dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1])

