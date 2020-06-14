class UndergroundSystem:
    trips = {}
    customers = {}
    def __init__(self):
        return

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers:
            curr = self.customers[id]
            travel = (curr[0], stationName)
            if travel in self.trips:
                self.trips[travel][0] += t - curr[1]
                self.trips[travel][1] += 1
            else:
                self.trips[travel] = [t - curr[1], 1]
        self.customers[id] = [stationName, t]   

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers:
            curr = self.customers[id]
            travel = (curr[0], stationName)
            if travel in self.trips:
                self.trips[travel][0] += t - curr[1]
                self.trips[travel][1] += 1
            else:
                self.trips[travel] = [t - curr[1], 1]
        self.customers[id] = [stationName, t]          

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.trips[(startStation, endStation)][0] / self.trips[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
