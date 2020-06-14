class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 0
        if n < 1:
            return False
        while n:
            res += n & 1
            n >>= 1
        return res == 1
