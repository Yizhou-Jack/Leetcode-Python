# 构建二维dp数组
dp=[[0]*5 for _ in range(5)]

# 表示很大的一个值
testInt = float('inf')

# 构建directions数组
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]