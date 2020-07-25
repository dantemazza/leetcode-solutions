class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = defaultdict(int)
        for word in words:
            freq_map[word] += 1
        return sorted(freq_map, key = lambda k: (-freq_map[k], k))[:k]
            
