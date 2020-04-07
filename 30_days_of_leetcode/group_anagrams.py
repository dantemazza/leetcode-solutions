class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        
        for i in strs:
            x[tuple(sorted(i))].append(i)
        
        res = []
        for i in x: 
            res.append(list(x[i]))
        return res
