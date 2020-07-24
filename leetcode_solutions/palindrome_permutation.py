class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq_map = defaultdict(int)
        
        for ch in s:
            freq_map[ch] += 1

        num_odd = False
        
        for k, v in freq_map.items():
            if v % 2:
                if num_odd or not len(s) % 2:
                    return False
                num_odd = True
        
        return True
