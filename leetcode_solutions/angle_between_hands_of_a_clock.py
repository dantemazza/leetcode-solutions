class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes * 6
        h = (hour % 12 + minutes/60) * 30
        angle = abs(h-m)
        return angle if angle <=180 else 360-angle
