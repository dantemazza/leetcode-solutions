class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        mid = ['a','s','d','f','g','h','j','k','l']
        btm = ['z','x','c','v','b','n','m']
        rows = [top, mid, btm]
        row = 0
        res = []
        for i in words:
            for e, z in enumerate(rows):
                if i[0].lower() in z:
                    row = e
                    break
            add = True
            for x in i[1:]:
                if not x.lower() in rows[row]:
                    add = False
                    break
            if add:
                res.append(i)
        return res
                
                        
