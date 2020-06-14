class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i in range(len(nums)-1):
            map[nums[i]] = i

            if target - nums[i+1] in map.keys():
                return [i+1, map[target-nums[i+1]]]

        
