class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            bit1 = x & 1
            bit2 = y & 1
            res += bit1 ^ bit2
            x >>= 1
            y >>= 1
        return res
    
