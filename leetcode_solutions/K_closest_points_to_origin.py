class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = []
        for point in points:
            heappush(pq, (math.sqrt(point[0]**2+point[1]**2), point))
        res = []
        for i in range(K):
            distance, point = heappop(pq)
            res.append(point)
        return res
