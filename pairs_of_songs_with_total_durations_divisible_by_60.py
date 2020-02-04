class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        amap = {}
        res = 0
        for i in time:
            if amap.get(60 - i % 60):
                res += amap[60 - i % 60]
            if i % 60 == 0 and amap.get(0):
                res += amap[0]
            if not amap.get(i % 60):
                amap[i % 60] = 1
            else:
                amap[i % 60] += 1
            
        return res
