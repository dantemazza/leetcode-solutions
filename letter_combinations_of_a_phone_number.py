class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        amap = {'2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}

        res = amap[digits[0]]
        curr = []
        for i in digits[1:]:
            for j in res:
                for k in amap[i]:
                    curr.append(j+k)
            res = curr
            curr= []
            
            
        return res
        
        
        
