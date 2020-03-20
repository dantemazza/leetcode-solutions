class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        x = '0-1-2-3-4-5-6-7-8-9'.split('-')
        res = 0
        zero = 0
        neg = 1
        plus = 0
        for i in str:
            if not zero and not plus and not neg == -1:
                if i =='-':
                    neg *= -1
                    zero = 1
                    continue
                elif i == '+':
                    plus = 1
                    zero = 1
                    continue
            if i in x:
                zero = 1
                res *= 10
                res += int(i)
            elif i != ' ' or zero:
                break
                

        res *= neg
        if res < 0:
            return max(res, -pow(2,31))

        return min(res, pow(2,31)-1)
