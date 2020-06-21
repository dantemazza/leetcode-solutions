class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dp = [[False]*len(board[0]) for i in range(len(board))]
        
        def dfs(i, j, s, e):
            nonlocal word
            nonlocal board
            nonlocal dp
            dp[i][j] = True
            if s==e:
                return True
            if i > 0:
                if board[i-1][j] == word[s] and not dp[i-1][j]:
                    if dfs(i-1, j, s+1, e):
                        return True
            if i < len(board)-1:
                if board[i+1][j] == word[s] and not dp[i+1][j]:
                    if dfs(i+1, j, s+1, e):
                        return True
            if j < len(board[0])-1:
                if board[i][j+1] == word[s] and not dp[i][j+1]:
                    if dfs(i, j+1, s+1, e):
                        return True
            if j > 0:
                if board[i][j-1] == word[s] and not dp[i][j-1]:
                    if dfs(i, j-1, s+1, e):
                        return True
            dp[i][j] = False
            return False
                  
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, len(word)):
                        return True
        return False
