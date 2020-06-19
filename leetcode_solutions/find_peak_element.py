class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums)-1
        mid = (end+start)//2

        while start != end:
            if nums[mid] > nums[mid+1]:
                if nums[mid] > nums[mid-1]:
                    return mid
                end = mid-1
            else:
                start=mid+1
            mid = (start + end) // 2
        return start
