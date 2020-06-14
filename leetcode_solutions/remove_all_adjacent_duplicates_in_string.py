class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        while True:
            s = S
            dup = False
            for e in range(len(s)-1):
                if s[e] == s[e+1]:
                    S = S.replace(S[e:e+2], '')
                    dup = True
                    break
            if not dup:
                return S
