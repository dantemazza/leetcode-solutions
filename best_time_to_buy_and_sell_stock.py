class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        lower = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[lower] > profit:
                profit = prices[i]-prices[lower]
            elif prices[i] < prices[lower]:
                lower = i
        
        return profit
                    
        
