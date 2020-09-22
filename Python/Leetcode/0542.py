import copy

def updateMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(matrix)
    m = len(matrix[0])
    res = [[float('inf')]*m for _ in range(n)]
    for i in range(n):
        distance = float('inf')
        for j in range(m):
            if matrix[i][j] == 0:
                res[i][j] = 0
                distance = 0
            else:
                distance += 1
                res[i][j] = distance
        distance = float('inf')
        for j in range(m-1, -1, -1):
            if matrix[i][j] == 0:
                distance = 0
            else:
                distance += 1
                res[i][j] = min(distance, res[i][j])
    for j in range(m):
        distance = float('inf')
        for i in range(n):
            if matrix[i][j] == 0:
                distance = 0
            else:
                distance += 1
                res[i][j] = min(distance, res[i][j])
        distance = float('inf')
        for i in range(n-1, -1, -1):
            if matrix[i][j] == 0:
                distance = 0
            else:
                distance += 1
                res[i][j] = min(distance, res[i][j])
    realRes = copy.deepcopy(res)
    for i in range(n):
        for j in range(m):
            if res[i][j] == 0:
                continue
            else:
                ansList = []
                if i-1 > 0: ansList.append(res[i-1][j])
                if i+1 < n: ansList.append(res[i+1][j])
                if j-1 > 0: ansList.append(res[i][j-1])
                if j+1 < m: ansList.append(res[i][j+1])
                if len(ansList) > 0: realRes[i][j] = min(res[i][j], min(ansList)+1)
    return realRes

matrix = [[0,0,1,0,1,1,1,0,1,1],
          [1,1,1,1,0,1,1,1,1,1],
          [1,1,1,1,1,0,0,0,1,1],
          [1,0,1,0,1,1,1,0,1,1],
          [0,0,1,1,1,0,1,1,1,1],
          [1,0,1,1,1,1,1,1,1,1],
          [1,1,1,1,0,1,0,1,0,1],
          [0,1,0,0,0,1,0,0,1,1],
          [1,1,1,0,1,1,0,1,0,1],
          [1,0,1,1,1,0,1,1,1,0]]
print(updateMatrix(matrix))