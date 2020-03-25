class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target in nums else -1
        lower = 0
        upper = len(nums) - 1
        mid = (upper + lower) /2
        if nums[lower] < nums[upper]: 
            return self.binarySearch(nums, target, lower, upper)
        while upper != lower+1:
            if nums[mid] > nums[upper]:
                lower = mid
            else:
                upper = mid
            mid = (lower+upper)/2
        if nums[-1] >= target:
            return self.binarySearch(nums, target, upper, len(nums)-1)
        else:
            return self.binarySearch(nums, target, 0, lower)
    def binarySearch(self, nums, target, lower, upper):
        print(upper, lower)
        if upper == lower:
            return upper if nums[upper] == target else -1
        if upper < lower:
            return -1
        mid = (upper+lower)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
             return self.binarySearch(nums, target, lower, mid-1)
        else:
             return self.binarySearch(nums, target, mid+1, upper)
        return -1
