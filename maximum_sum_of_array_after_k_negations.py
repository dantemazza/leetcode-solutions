class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        p = sorted(A)
        index = 0
        for i in range(len(p)):
            if K > 0:
                if p[i] < 0:
                    p[i] *= -1
                else:
                    break
                K -= 1
            else:
                print(p)
                return sum(p)
        p = sorted(p)
        if K % 2 != 0:
            p[0] *= -1
            
        return sum(p)
            
            
                    
            
            
