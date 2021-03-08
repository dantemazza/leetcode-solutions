class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        return max(self._rob(nums, 1, len(nums)-1, memo),
                  self._rob(nums, 0, len(nums)-2, memo))
    
    
    def _rob(self, nums, i, j, memo):
        if i == j:
            return nums[i]
        if i > j or j < i: 
            return 0
        
        if (i,j) in memo:
            return memo[(i, j)]
        inc = max(nums[i] + self._rob(nums, i+2, j, memo), nums[j] + self._rob(nums, i, j-2, memo))
        exc = max(self._rob(nums, i+1, j, memo), self._rob(nums, i, j-1, memo))
        memo[(i,j)] = max(inc, exc)
        return memo[(i,j)]
