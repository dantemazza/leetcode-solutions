class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        
        res = [('(', 1, 0)]
        curr = []
        for i in range(2*n-1):
            for j in res:
                if j[1] < n:
                    curr.append((j[0] + '(', j[1] + 1, j[2]))
                if j[2] < j[1]:
                    curr.append((j[0] + ')', j[1], j[2] + 1))
            res = curr
            curr = []
        return [res[i][0] for i in range(len(res))]
               
