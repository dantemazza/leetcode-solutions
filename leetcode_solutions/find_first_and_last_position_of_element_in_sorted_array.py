class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenums = len(nums)
        res = -1
        lower = 0
        upper = lenums - 1
        while upper >= lower:
            mid = (upper + lower)/2
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                lower = mid+1
            else:
                upper = mid-1
        l = res
        u = res
        
        while True:
            if u < lenums-1:
                if nums[u+1] == target:
                    u += 1
                    continue
            break  
        while True:
            if l > 0:
                if nums[l-1] == target:
                    l -= 1
                    continue
            break
        return [l, u]
