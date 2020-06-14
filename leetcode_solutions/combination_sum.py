class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        def getCombos(n, target):
            nonlocal candidates
            nonlocal res
            nonlocal stack
            if n == len(candidates) or target < 0:
                if stack:
                    stack.pop()
                return 
            if target == 0: 
                res.append(stack.copy())
                if stack:
                    stack.pop()
                return
            stack.append(candidates[n])
            getCombos(n, target-candidates[n])
            getCombos(n+1, target)
        
        getCombos(0, target)
        return res
