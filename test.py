n = int(input())
m = int(input())
grid = [ [ ] for a in range(n)]
for i in range(n):
	grid[i] = [int(x) for x in input().split(' ')]

def valid(r,c,n,m,a,b,grid):
	return True if not (a>=0 and a<n and b>=0 and b<m) or grid[a][b]<grid[r][c] else False

def numCells(grid):
	counter = 0
	n = len(grid)
	m = len(grid[0])
	for r in range(n):
		for c in range(m):
			if valid(r,c,n,m,r-1,c-1,grid) and valid(r,c,n,m,r-1,c,grid) and valid(r,c,n,m,r-1,c+1,grid) and valid(r,c,n,m,r,c-1,grid) and valid(r,c,n,m,r,c+1,grid) and valid(r,c,n,m,r+1,c-1,grid) and valid(r,c,n,m,r+1,c+1,grid) and valid(r,c,n,m,r+1,c,grid):

				counter += 1

	return counter


print(numCells(grid))
