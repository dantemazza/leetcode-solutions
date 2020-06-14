class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        closed = 0
        for i in S:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    closed += 1
        return len(stack) + closed
