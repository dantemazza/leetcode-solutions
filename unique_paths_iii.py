class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = []
        end = []
        zeros = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = [i, j]
                if grid[i][j] == 2:
                    end = [i, j]
                if not grid[i][j]:
                    zeros += 1
        paths = [0]
        def getNumPaths(grid, i, j, depth):
            if i > 0:
                if grid[i-1][j] == 2:
                    paths[0] += 1 if depth == zeros else 0
                if not grid[i-1][j]:
                    grid[i-1][j] = 1
                    getNumPaths(grid, i-1, j, depth+1)
                    grid[i-1][j] = 0   
            if i < len(grid)-1:
                if grid[i+1][j] == 2:
                    paths[0] += 1 if depth == zeros else 0
                if not grid[i+1][j]:
                    grid[i+1][j] = 1
                    getNumPaths(grid, i+1, j, depth+1)
                    grid[i+1][j] = 0          
            if j > 0:
                if grid[i][j-1] == 2:
                    paths[0] += 1 if depth == zeros else 0
                if not grid[i][j-1]:
                    grid[i][j-1] = 1
                    getNumPaths(grid, i, j-1, depth+1)
                    grid[i][j-1] = 0   
            if j < len(grid[0])-1:
                if grid[i][j+1] == 2:
                    paths[0] += 1 if depth == zeros else 0
                if not grid[i][j+1]:
                    grid[i][j+1] = 1
                    getNumPaths(grid, i, j+1, depth+1)
                    grid[i][j+1] = 0  
        
        getNumPaths(grid, start[0], start[1], 0)
        return paths[0]
    
