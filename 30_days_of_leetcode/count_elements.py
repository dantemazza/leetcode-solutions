class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set()
        for i in arr:
            nums.add(i)
        res = 0
        for i in arr:
            if i+1 in nums:
                res += 1
        return res
