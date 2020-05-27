class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        res = 0
        def play(N, K, W, start, depth):
            nonlocal res
            if start >= K:
                if start <= N:
                    res += 1/(pow(W, depth))
                return
            for w in range(1, W+1):
                play(N, K, W, start+w, depth+1)

        play(N, K, W, 0, 0)
        return res
