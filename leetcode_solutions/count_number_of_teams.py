class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        more = defaultdict(int)
        less = defaultdict(int)
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                    if rating[i] < rating[j]:
                        more[(rating[i], rating[j])] = j
                    if rating[i] > rating[j]:
                        less[(rating[i], rating[j])] = j

        for i in more.keys():
            for j in range(more[i]+1, len(rating)):
                if rating[j] > i[1]:
                    res += 1
        
        for i in less.keys():
            for j in range(less[i]+1, len(rating)):
                if rating[j] < i[1]:
                    res += 1
        
        
        return res
