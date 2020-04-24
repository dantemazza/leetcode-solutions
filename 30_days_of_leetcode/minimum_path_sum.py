class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
        return self.getMin(0,0,grid, memo) 
            
    def getMin(self, down, right, grid, memo):
        res = 0
        if memo[down][right]:
            return memo[down][right]
        if down == len(grid) - 1:
            for i in range(right, len(grid[0])):
                res += grid[-1][i]
            return res
        if right == len(grid[0]) - 1:
            for i in range(down, len(grid)):
                res += grid[i][-1]
            return res
        memo[down][right] = grid[down][right] + min(self.getMin(down+1, right, grid, memo), self.getMin(down, right+1, grid, memo))
        return memo[down][right]
