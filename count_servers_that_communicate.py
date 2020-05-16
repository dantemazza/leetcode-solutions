class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        X = 0
        pow10 = 1
        for digit in reversed(A):
            X += digit*pow10
            pow10 *= 10
        
        K += X
        length = len(str(K))
        res = [None for i in range(length)]
        
        pow10 = 10
        for i in reversed(range(length)):
            num = (K % pow10)
            res[i] = num
            K -= num
            K //= 10
        return res
            
