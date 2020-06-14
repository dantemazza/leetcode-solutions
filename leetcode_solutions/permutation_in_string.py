class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return 0
        amap = defaultdict(int)
        for ch in s1:
            amap[ch] += 1
        
        bmap = defaultdict(int)
        for i in range(len(s1)):
            bmap[s2[i]] += 1
        
        for i in range(len(s1), len(s2)):
            same = True
            for key in amap.keys():
                if amap[key] != bmap[key]:
                    same = False
                    break
            if same:
                return same
            bmap[s2[i-len(s1)]] -=1
            bmap[s2[i]] += 1
        
        same = True
        for key in amap.keys():
            if amap[key] != bmap[key]:
                same = False
                break
        return same
