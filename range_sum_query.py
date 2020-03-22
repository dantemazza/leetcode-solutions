class NumArray:
    numarr = [0]
    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.numarr[0] = nums[0]
        for i in range(1, len(nums)):
            self.numarr.append(nums[i] + self.numarr[i-1])

    def sumRange(self, i: int, j: int) -> int:
        lower = 0 if not i else self.numarr[i-1]
        return self.numarr[j] - lower


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
