class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []
        o = 0
        for i in s:
            if i == '(':
                stack.append(0)
                o += 1
            else:
                if not o:
                    if stack:
                        curr = stack.pop()
                        res = max(curr, res)
                    continue
                o-=1
                if len(stack) == 1:
                    stack[-1] += 2
                    continue
                curr = stack.pop() + 2
                stack[-1] += curr
        if stack:
            return max(res, max(stack)) 
        return res
        
                    
        
