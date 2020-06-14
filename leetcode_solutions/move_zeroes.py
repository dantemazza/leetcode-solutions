class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return 
        zero = -1
        num = 0
        lenums = len(nums)
        while num < lenums and zero < lenums:
            zero += 1
            while zero < lenums:
                if nums[zero] != 0:
                    zero += 1
                else:
                    break
            
            while num < lenums:
                if nums[num] == 0:
                    num += 1
                else:
                    if num > zero:
                        break
                    num += 1
            if zero < lenums and num < lenums and num > zero:
                nums[zero] = nums[num]
                nums[num] = 0

            
                
            
            
        
