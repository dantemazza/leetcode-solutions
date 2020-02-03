class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        xa1 = rec1[0]
        ya1 = rec1[1]
        xa2 = rec1[2]
        ya2 = rec1[3]
        
        xb1 = rec2[0]
        yb1 = rec2[1]
        xb2 = rec2[2]
        yb2 = rec2[3]
        
        x1 = ((xa1 > xb1) and (xb2 > xa1)) or ((xa2 > xb1) and (xb2 > xa2))
        x2 = ((xb1 > xa1) and (xa2 > xb1)) or ((xb2 > xa1) and (xa2 > xb2))
        y1 = ((ya1 > yb1) and (yb2 > ya1)) or ((ya2 > yb1) and (yb2 > ya2))
        y2 = ((yb1 > ya1) and (ya2 > yb1)) or ((yb2 > ya1) and (ya2 > yb2))
        
        return (x1 or x2) and (y1 or y2)
