class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        islands = 0 
        def island(i, j):
            if grid[i][j]:
                return 1
            if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                return 0
            grid[i][j] = 1
            up = island(i+1, j)
            down = island(i-1, j)
            left = island(i, j-1)
            right = island(i, j+1)
            return up and down and left and right
            
        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if not grid[i][j]:
                    islands += island(i, j)
        return islands
