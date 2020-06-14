class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        count = len(s)
        def build(start, end):
            nonlocal s
            nonlocal dp
            nonlocal count
            if not end-start:
                if end < len(s)-1 and s[end+1] == s[end] and not dp[end][end+1]:
                    dp[end][end+1] = 1
                    count += 1
                    build(end, end+1)
                if start > 0 and s[start-1] == s[start] and not dp[start-1][start]:
                    dp[start-1][start] = 1
                    count += 1
                    build(start-1, start)
            
            if dp[start][end] == 1:
                if start > 0 and end < len(s)-1:
                    if not dp[start-1][end+1] and s[start-1] == s[end+1]:
                        dp[start-1][end+1] = 1
                        count += 1
                        build(start-1, end+1)
                    
        for i in range(len(s)):
            build(i, i)
        return count
    
    
    
        
                
        
