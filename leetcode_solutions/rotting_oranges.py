class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
            
        def isFresh(i, j):
            nonlocal grid
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return None
            return grid[i][j] if grid[i][j] == 1 else None
        
        minutes=0
        while queue:
            if not fresh:
                return minutes
            minutes+=1
            qlen = len(queue) 
            for i in range(qlen):
                o = queue.popleft()
                if isFresh(o[0]+1, o[1]):
                    fresh -= 1
                    grid[o[0]+1][o[1]] = 2
                    queue.append((o[0]+1, o[1]))
                if isFresh(o[0]-1, o[1]):
                    fresh -= 1
                    grid[o[0]-1][o[1]] = 2
                    queue.append((o[0]-1, o[1]))
                if isFresh(o[0], o[1]+1):
                    fresh -= 1
                    grid[o[0]][o[1]+1] = 2
                    queue.append((o[0], o[1]+1))
                if isFresh(o[0], o[1]-1):
                    fresh -= 1
                    grid[o[0]][o[1]-1] = 2
                    queue.append((o[0], o[1]-1))
        return minutes if not fresh else -1
            
