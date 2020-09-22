def checkWalls(walls, targets, length):
    p1 = p2 = 0
    while p1 < length and p2 < length:
        if walls[p1] != targets[p2]:
            p1 += 1
        else:
            p2 += 1
    if p2 == length:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    walls = list(map(int, input().split(" ")))
    targets = list(map(int, input().split(" ")))
    print(checkWalls(walls, targets, n))