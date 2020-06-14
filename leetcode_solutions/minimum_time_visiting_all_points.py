class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)-1):
            currX = abs(points[i+1][0] - points[i][0])
            currY = abs(points[i+1][1] - points[i][1])
            res += max(currX, currY)
            
        return res
