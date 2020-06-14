class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, visited, i, j)
                    res += 1
        return res
    
    def dfs(self, grid, visited, i, j):
        if grid[i][j] == "0" or visited[i][j]:
            return
        visited[i][j] = 1
        if i - 1 >=0:
            self.dfs(grid, visited, i-1, j)
        if j - 1 >=0:
            self.dfs(grid, visited, i, j-1)
        if i+1 < len(grid):
            self.dfs(grid, visited, i+1, j)
        if j+1 < len(grid[0]):
            self.dfs(grid, visited, i, j+1)
        
            
        
