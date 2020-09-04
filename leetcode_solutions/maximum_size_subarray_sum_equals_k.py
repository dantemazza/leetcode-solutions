class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        _map = {nums[0]: 0}
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] not in _map:
                _map[nums[i]] = i
            
        res = 0
        print(nums)
        for i, num in enumerate(nums):
            if num == k:
                res = max(res, i+1)
            if num-k in _map and _map[num-k] < i:
                res = max(res, i-_map[num-k])
        
        return res
