class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        res = 0
        curr = prices[0]
        
        for i in prices[1:]:
            if i > curr:
                res += i-curr
            curr = i
        return res
        
