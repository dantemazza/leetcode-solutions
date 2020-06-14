class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        for i in emails:
            parts = i.split('@')
            parts[0] = ''.join(parts[0].split('.'))
            parts[0] = parts[0].split('+')[0]
            parts[0] += '@'
            res.append(''.join(parts))
        return len(list(set(res)))
