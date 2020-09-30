class Solution:      
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        start = 0
        end = len(nums)-1
        mid = (start+end) // 2
        
        while start != end:
            if mid > 0:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
            if mid < len(nums)-1:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
            
            if nums[start] < nums[mid]:
                start = mid
                mid = (start + end) // 2
            else:
                end = mid
                mid = (start + end) // 2
        return nums[0]
                
