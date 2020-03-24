class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            p = ""
            res = self.countaz(p, res)
        return res
    
    def countaz(self, res, n):
        if not n:
            return res
        c = n[0]
        for i in n[1:]:
            if c[0] != i:
                break
            else:
                c += i
        res += str(len(c)) + c[0]
        return self.countaz(res, n[len(c):])
            
