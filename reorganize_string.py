class Solution:
    def reorganizeString(self, S: str) -> str:
        letters = defaultdict(int)
        res = [None] * len(S)
        for s in S:
            letters[s] += 1
            
        last = ''
        letterMax = ['', 0]
        for p in range(len(S)):
            letterMax[1] = 0
            for l in letters:
                if letters[l] > letterMax[1] and last != l:
                    letterMax = [l, letters[l]]
            if last == letterMax[0]:
                return ""
            last = letterMax[0]
            res[p] = letterMax[0]
            letters[letterMax[0]] -= 1
        return ''.join(res)
