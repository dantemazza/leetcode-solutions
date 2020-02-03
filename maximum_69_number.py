class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        stint = list(str(num))
        
        for e, i in enumerate(stint):
            if i == '6':
                stint[e] = '9'
                return int(''.join(stint))
        return num
