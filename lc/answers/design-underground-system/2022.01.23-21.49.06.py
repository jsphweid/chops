class UndergroundSystem:

    def __init__(self):
        # {str-str: (total, total_min)}
        self.times = {}

        # {person_id: (check_in: str, check_in_time: int)}
        self.people = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin, checkin_time = self.people[id]
        key, time = (f"{checkin}-{stationName}", t - checkin_time)
        self.people[id] = None
        curr_total, curr_total_min = self.times[key] if key in self.times else (0, 0)
        self.times[key] = (curr_total + 1, curr_total_min + time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, total_min = self.times[f"{startStation}-{endStation}"]
        return total_min / total

