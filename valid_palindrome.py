class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(e for e in s if e.isalnum())
        if s.isspace():
            return true
        return s.lower() == s[::-1].lower()
        
