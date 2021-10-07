# Note for Format
## Grid
*	row, col = len(grid), len(grid[0])
*	visited = [[0]*col for _ in range(row)]
*	Use i, j as index in the nested for loop
*	Check new row and new col expand in four directions: DIR = [0, 1, 0, -1, 0]