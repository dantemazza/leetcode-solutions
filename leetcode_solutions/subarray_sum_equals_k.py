class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        freq = defaultdict(int)
        res = 0
        freq[nums[0]] = 1
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            freq[nums[i]] += 1
        for num in reversed(nums):
            freq[num] -= 1;
            if num == k:
                res += 1
                if k:
                    continue
            res += freq[num-k]
            
            
        
            
        return res
