class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        amap = {}
        res = n
        while res !=1:
            num = res
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            if amap.get(res):
                return False
            amap[res] = True
            
            
        return True
        
        
