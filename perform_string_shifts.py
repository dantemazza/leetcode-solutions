class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        toTheRight = 0
        for i, j in shift:
            toTheRight += -j if i else j
        toTheRight %= len(s)
        return s[toTheRight:] + s[0:toTheRight]
