class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        sortB = sorted(B)
        amap = {}
        a_index = len(B)-1
        for num in reversed(sortB):
            if num < A[a_index]:
                if not num in amap:
                    amap[num] = [A[a_index]]
                else:
                    amap[num].append(A[a_index])
                a_index -= 1
        res = []
        a_index = 0
        for num in B:
            if num in amap:
                if len(amap[num]) > 0:
                    res.append(amap[num].pop())
                    continue
            res.append(A[a_index])
            a_index += 1
            
            
        return res
            
                
                    
        
