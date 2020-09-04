class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num = 0
        for i in arr:            
            if i % 2:
                num += 1
            else:
                num = 0
            if num == 3:
                return True
        return False
