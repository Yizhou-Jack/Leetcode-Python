"""
Find up, down, left and right grid elements for one element in the grid
"""

grid = [[0,0,1], [1,0,0], [0,1,0]]

row = len(grid)
col = len(grid[0])
DIR = [0, 1, 0, -1, 0]
for r in range(row):
    for c in range(col):
        for i in range(4):
            nr, nc = r+DIR[i], c+DIR[i+1]
            if nr < 0 or nr == row or nc < 0 or nc == col: continue