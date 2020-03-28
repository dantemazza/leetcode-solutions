class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = {}
        A = 0
        B = 0
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                if i in x:
                    x[i] += 1
                else:
                    x[i] = 1
        for j, i in zip(secret, guess):
            if i == j:
                continue
            if i in x:
                if x[i] > 0:
                    B += 1
                    x[i] -= 1
        return f"{A}A{B}B"
        
