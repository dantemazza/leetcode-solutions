class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        curr = []
        length = len(candidates)
        def dp(n, amount):
            nonlocal res
            nonlocal curr
            nonlocal candidates
            nonlocal length
            if n == length or amount <= 0:
                if amount == 0:
                    res.add(tuple(sorted(curr[:])))
                if curr:
                    curr.pop()
                return 


            curr.append(candidates[n])
            dp(n+1, amount-candidates[n])
            dp(n+1, amount)
        
        dp(0, target)
        return list([list(x) for x in res])
