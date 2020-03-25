class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        amap = {}
        for i in S:
            if i not in amap:
                amap[i] = len(res)
                res.append(i) 
            else:
                p = ''.join(res[amap[i]:]+[i]) 
                for j in amap.keys():
                    if amap[j] > amap[i]:
                        amap[j] = amap[i]
                res = res[0:amap[i]]
                res.append(p)
        return [len(i) for i in res]
