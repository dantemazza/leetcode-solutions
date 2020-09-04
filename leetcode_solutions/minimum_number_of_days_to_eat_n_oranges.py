class Solution:
    def minDays(self, n: int) -> int:
        def eat1(n):
            return n-1
        
        
        def eat2(n):
            if not n % 2:
                return n/2
            return None
        
        
        def eat3(n):
            if not n % 3:
                return n/3
            return None
        
        memo = {}
        memo[0] = 0
        def eat(n):
            nonlocal memo
            if n in memo:
                return memo[n]
            if eat2(n):
                if eat3(n):
                    memo[n] = 1 + min(eat(eat2(n)), eat(eat3(n)))
                    return memo[n]
                memo[n] = 1+ min(eat(eat1(n)), eat(eat2(n)))
                return memo[n]
            if eat3(n):
                memo[n] = 1 + min(eat(eat1(n)), eat(eat3(n)))
                return memo[n]
            return 1 + eat(eat1(n))
                    
        return eat(n)
