class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        abc_order = {i: j for j, i in enumerate(order)}
        def is_sorted_pair(str1, str2):
            nonlocal abc_order
            for i, j in zip(str1, str2):
                if abc_order[i] < abc_order[j]:
                    return True
                elif abc_order[i] > abc_order[j]:
                    return False
            return len(str2) > len(str1)
        
        for i in range(len(words)-1):
            if not is_sorted_pair(words[i], words[i+1]):
                return False
        return True
