class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.solve(board)
        
    
    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in range(1, 10): 
                        if self.validate(board, r, c, str(num)):
                            board[r][c] = str(num)
                            if self.solve(board):
                                return True
                            board[r][c] = '.'
                    return False
        return True
    
    def validate(self, board, i, j, num): 
        nums = [num for num in board[i] if num != '.']
        nums.append(num)      
        if len(nums) != len(set(nums)):
            return False
        nums = [row[j] for row in board if row[j] != '.']
        nums.append(num)      
   
        if len(nums) != len(set(nums)):
            return False
        
        i -= i%3
        j -= j%3
        
        nums = {num}
        
        for row in range(i, i+3):
            for column in range(j, j+3):
                if board[row][column] == '.':
                    continue
                if board[row][column] in nums:
                    return False
                nums.add(board[row][column])
        return True
