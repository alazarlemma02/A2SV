# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkin_map = {}
        self.udg_map = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_map[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin = self.checkin_map[id]
        key = f"{checkin[0]} {stationName}"
        t_dif = t - checkin[1]
        if key in self.udg_map:
            self.udg_map[key] += [t_dif]
        else:
            self.udg_map[key] = [t_dif]   

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f"{startStation} {endStation}"
        trip_times = self.udg_map[key]
        average_time = sum(trip_times) / len(trip_times)
        return average_time
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)