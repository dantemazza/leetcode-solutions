class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x = coordinates[0][0]
        y = coordinates[0][1]
        deltax = abs(coordinates[1][0] - coordinates[0][0])
        deltay = abs(coordinates[1][1] - coordinates[0][1])
        slope = sys.maxsize
        if deltax:
            slope = deltay / deltax;
        for c in range(2, len(coordinates)):
            if not abs(coordinates[c][0] - x):
                if slope == sys.maxsize:
                    continue
                else:
                    return False
            if abs(coordinates[c][1] - y) / abs(coordinates[c][0] - x) != slope:
                return False
        return True
