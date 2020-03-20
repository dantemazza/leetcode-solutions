class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        memo = {1 : 1, 2 : 2}
        return self.dp(n, memo)
        
    
    def dp(self, n, memo):
        if memo.get(n):
            return memo[n]    
        memo[n-1] = self.dp(n-1, memo)
        memo[n-2] = self.dp(n-2, memo)
        return self.dp(n-1, memo) + self.dp(n-2, memo)
        
