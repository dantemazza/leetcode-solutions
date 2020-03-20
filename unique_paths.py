class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [1 for x in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                memo[j] += memo[j-1]
        return memo[-1]    
                
