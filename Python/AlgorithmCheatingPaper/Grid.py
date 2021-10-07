"""
Find up, down, left and right grid elements for one element in the grid
"""

grid = [[0,0,1], [1,0,0], [0,1,0]]

row, col = len(grid), len(grid[0])
DIR = [0, 1, 0, -1, 0]
for i in range(row):
    for j in range(col):
        for k in range(4):
            nr, nc = i+DIR[k], j+DIR[k+1]
            if nr < 0 or nr == row or nc < 0 or nc == col: continue