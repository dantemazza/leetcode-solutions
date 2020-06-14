class Solution:
    def countBits(self, num: int) -> List[int]:
        curr = 1
        res = [0]
        while True:
            for e, i in enumerate(range(curr, 2*curr)):
                if i > num:
                    return res
                res.append(res[e]+1)
            curr *=2
        return res            
