class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = [(i, abs(x[1] - x[0])) for i, x in enumerate(costs)]
        differences.sort(key=lambda x: x[1], reverse=True)
        res = 0
        N = len(costs) / 2
        A = 0 
        B = 0
        for i, x in differences:
            if costs[i][0] > costs[i][1] and B < N or A == N:  
                B += 1
                res += costs[i][1]
            else:
                A +=1 
                res += costs[i][0]
        return res
