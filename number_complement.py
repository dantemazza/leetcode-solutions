class Solution:
    def findComplement(self, num: int) -> int:
        comp = 1
        while comp <= num:
            num ^= comp
            comp <<= 1
        return num
