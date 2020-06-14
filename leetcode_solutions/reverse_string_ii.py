class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        lower = 0
        upper = min(k, len(s))
        reverse = True
        while len(res) != len(s):
            sub = s[lower:upper]
            if reverse:
                res += sub[::-1]
            else:
                res += sub
            lower = upper
            upper = min(upper+k, len(s))
            reverse = not reverse
        return res
