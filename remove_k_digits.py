class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if not num or k == len(num):
            return "0"
        for index, digit in enumerate(num):
            digit = int(digit)
            if not stack or not k:
                stack.append(digit)
            else:
                while digit < stack[-1]:
                    stack.pop()
                    k -= 1
                    if not stack or not k:
                        break
                stack.append(digit)
        while k and stack:
            k -= 1
            stack.pop()
        return str(int(''.join([str(i) for i in stack])))
            
