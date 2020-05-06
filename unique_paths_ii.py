class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        dp = [0 for i in range(len(obstacleGrid[0]))]
            
        for j in range(len(obstacleGrid[0])):
            if not obstacleGrid[0][j]:
                dp[j] = 1
            else:
                break      
        columnBlock = obstacleGrid[0][0]
        for i in range(1, len(obstacleGrid)):
            columnBlock = columnBlock or obstacleGrid[i][0]
            dp[0] = 0 if columnBlock else 1
            for j in range(1, len(obstacleGrid[0])):
                if not obstacleGrid[i][j]:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0
        return dp[-1]
