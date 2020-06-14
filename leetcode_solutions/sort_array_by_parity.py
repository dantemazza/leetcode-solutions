class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in A:
            if(not i % 2):
                even.append(i)
            else:
                odd.append(i)
                
        return even + odd
