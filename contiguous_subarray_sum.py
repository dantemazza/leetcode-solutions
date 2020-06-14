class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: 
            return False
        def specmod(num, k):
            if not k:
                return num
            return num % k
        hashset = set()
        hashset.add(0)
        hashset.add(specmod(nums[0], k))
        firstTwo = [nums[0], nums[1]]

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if specmod(nums[i], k) in hashset:
                if specmod(nums[i], k) != specmod(nums[i-1], k):
                    return True
                else:
                    if i > 1:
                        if specmod(nums[i], k) == specmod(nums[i-2], k):
                            return True
                    else:
                        if specmod(firstTwo[0], k) == specmod(firstTwo[1], k):
                            return True
            hashset.add(specmod(nums[i], k))
        return False
    
    
