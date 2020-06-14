class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        for i in reversed(range(length)):
            if nums[i] == val: 
                del nums[i]
        
        return len(nums)
