class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        results = []
        
        
        for L in [S, T]:
            res = ""
            back = 0
            for r in L:
                if r == '#':
                    back += 1
                else:
                    if back:
                        if back >= len(res):
                            res = ""
                        else:
                            res = res[:-back]
                        back = 0
                    res += r   
            results.append(res[:-back] if back else res)
        return results[0] == results[1]
        
