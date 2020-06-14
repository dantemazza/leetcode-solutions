class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, u = 0, len(A)-1
        m = (u+l)/2
        while(u != l+1):
            if A[m] < A[m+1]:
                l = m
            else:
                u = m
            m = (u+l)/2
                
        return u
            
                
            
