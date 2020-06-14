class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            nums = [num for num in i if num != '.']
            if len(nums) != len(set(nums)):
                return False
        for j in range(len(board[0])):
            nums = [row[j] for row in board]
            nums = [num for num in nums if num != '.']
            if len(nums) != len(set(nums)):
                return False
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                nums = set()
                for row in range(i,i+3):
                    for column in range(j, j+3):
                        if board[row][column] == '.':
                            continue
                        if board[row][column] in nums:
                            return False
                        nums.add(board[row][column])
        return True
