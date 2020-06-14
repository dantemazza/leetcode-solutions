class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        cmap = {0: -1}
        res = 0
        for index, num in enumerate(nums):
            if num:
                count += 1
            else:   
                count -= 1
            if not count in cmap:
                cmap[count] = index
            else:
                res = max(res, index-cmap[count])
        return res
