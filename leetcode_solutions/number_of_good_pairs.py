class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        res = 0
        for num in nums:
            if num in freq_map:
                res += freq_map[num]
            freq_map[num] += 1
        return res
