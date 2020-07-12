class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        curr = 0 
        for i in s:
            if i == '1':
                curr += 1
            else:
                res += curr*(curr+1)/2
                curr = 0
        return int(res + curr*(curr+1)/2) % (10**9+7)
                    
