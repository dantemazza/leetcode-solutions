class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        res = 0
        charset = set()
        while end < len(s):
            if s[end] in charset:
                res = max(res, end-start)
                while s[start] != s[end]:
                    charset.remove(s[start])
                    start += 1
                start += 1
            charset.add(s[end])
            end += 1
        return max(res, end-start)
