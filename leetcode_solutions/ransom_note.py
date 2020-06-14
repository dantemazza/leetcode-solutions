class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomLetters = defaultdict(int)
        
        for ch in ransomNote:
            ransomLetters[ch] += 1
        for ch in magazine:
            ransomLetters[ch] -= 1
        for key, value in ransomLetters.items():
            if value > 0: 
                return False
        return True
