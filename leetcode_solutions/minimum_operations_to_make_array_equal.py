class Solution:
    def minOperations(self, n: int) -> int:
        return int(sum([abs(2*i+1-n) for i in range(n)])/2)
