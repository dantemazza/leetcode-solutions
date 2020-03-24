class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return 1
        jump = nums[0]
        for i in range(1,len(nums)):
            if not jump:
                return 0
            jump -= 1
            jump = jump if jump > nums[i] else nums[i]      
        return 1
            
        
