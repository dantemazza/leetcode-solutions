class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        depth = 0
        for i in S:
            if i == "(":
                stack.append(0)
            else:
                last = stack.pop()
                if not last:
                    stack.append(1)
                    continue
                asum = last
                while stack:
                    if not stack[-1]:
                        break
                    asum += stack.pop()
                if stack:
                    stack.pop()
                stack.append(2*asum)
                
        return sum(stack)
