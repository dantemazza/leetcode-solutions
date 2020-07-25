class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        o = 0
        del_closed = set()
        for i, ch in enumerate(s):
            if ch == '(':
                o += 1
            if ch == ')':
                if o:
                    o -= 1
                else:
                    del_closed.add(i)
        result = [None for i in range(len(s)-o-len(del_closed))]
        index = len(result)-1
        for i, ch in reversed(list(enumerate(s))):
            if i in del_closed:
                continue
            if ch == '(' and o:
                o -= 1
                continue
            else: 
                result[index] = ch
                index -= 1
                
        return ''.join(result)
