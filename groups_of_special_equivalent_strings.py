class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
     
        if not A:
            return 0

        length = len(A[0])
        words = set()
        for a in A:
            odd = []
            even = []
            isEven = True
            for index in range(length):
                if isEven:
                    even.append(a[index])
                else:
                    odd.append(a[index])
                isEven = not isEven
            words.add(''.join(sorted(odd) + sorted(even)))
        return len(words)
