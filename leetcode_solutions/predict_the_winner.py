class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = [[-1 for i in range(len(nums))] for j in range(len(nums))]
        maxFirst = self.maxScore(nums, True, 0, len(nums)-1, memo)
        return 2*maxFirst >= sum(nums)
        
    def maxScore(self, nums, first, i, j, memo):
        if memo[i][j] != -1:
            return memo[i][j]
        if len(nums) == 1:
            if first:
                return nums[0] 
            else:
                return 0
        max1 = self.maxScore(nums[1:], not first, i+1, j, memo)
        max2 = self.maxScore(nums[:-1], not first, i, j-1, memo)
        if first:
            memo[i][j] = max(max1+nums[0], max2+nums[-1])
        else:
            memo[i][j] = min(max1, max2)
        return memo[i][j]
        
        
