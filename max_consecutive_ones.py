class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr +=1
            else:
                if curr:
                    max = max if max > curr else curr
                    curr = 0
            
        return max if max > curr else curr
