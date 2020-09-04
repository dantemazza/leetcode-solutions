class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ch_to_int = {k: v for v, k in enumerate(list('0123456789'))}    
        int_to_ch = {k: v for k, v in enumerate(list('0123456789'))}    
        sum = 0
        for num in [num1, num2]:
            factor = 1
            for n in reversed(num):
                sum += factor * ch_to_int[n]
                factor *= 10
        result = []
        if sum == 0:
            return '0'
        while sum:
            dig = sum % 10
            result.append(int_to_ch[dig])
            sum -= dig
            sum //= 10

        result.reverse()
        return ''.join(result)
