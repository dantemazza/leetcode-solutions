class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        
        for i in arr:
            freq[i] += 1
            
        largest = -1
        for i in freq:
            if freq[i] == i:
                if i > largest:
                    largest = i
        return largest
