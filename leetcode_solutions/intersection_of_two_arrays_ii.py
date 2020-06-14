class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        big = nums1 if len(nums1) >= len(nums2) else nums2
        small = nums2 if big == nums1 else nums1
        
        nums = list(set([x for x in small if x in big]))
        res = []
        for i in nums:
            bc = big.count(i)
            sc = small.count(i)
            c = bc if bc < sc else sc
            res += [i for x in range(c)]
            
        return res
            
        
