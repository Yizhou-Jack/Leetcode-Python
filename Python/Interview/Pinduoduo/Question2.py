nAndm = input().split(" ")
n = int(nAndm[0])
m = int(nAndm[1])

matrix = [[0]*m for _ in range(n)]
for i in range(n):
    line = input().split(" ")
    for j in range(m):
        matrix[i][j] = int(line[j])
