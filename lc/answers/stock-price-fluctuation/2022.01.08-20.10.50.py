"""
===== Initial Thoughts =====


=== Brute Force Approach ===
store everything once in a mpa

~~Complexity Analysis
Time - O(n) for all retrieval operations
Space - O(n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


4,5,6,5
update(1, 10)
update(2, 5)
update(1, 3)
update(4, 2)
timestamp: price
d={}

state={1:3, 2:5} max=(10, 1) min=(5, 2)
latest=2

I wrote this but it TLE'ed

class StockPrice:

    def __init__(self):
        self.state = {}
        self.latest = -1
        self._reset_max_min()

    def _reset_max_min(self):
        # first val is stock price, second val is timestamp
        self.max_price = (-1, -1)
        self.min_price = (float("inf"), -1)        

    def update(self, timestamp: int, price: int) -> None:
        is_correction = timestamp in self.state
        # does it affect a max or min
        max_price, max_price_timestamp = self.max_price
        min_price, min_price_timestamp = self.min_price

        self.state[timestamp] = price
        self.latest = max(self.latest, timestamp)

        if is_correction and (max_price_timestamp == timestamp or min_price_timestamp == timestamp):
                self._reset_max_min()
                for t, p in self.state.items():
                    self.max_price = max(self.max_price, (p, t))
                    self.min_price = min(self.min_price, (p, t))
        else:
            self.max_price = max(self.max_price, (price, timestamp))
            self.min_price = min(self.min_price, (price, timestamp))

    def current(self) -> int:
        return self.state[self.latest]

    def maximum(self) -> int:
        return self.max_price[0]

    def minimum(self) -> int:
        return self.min_price[0]


So I thought about an OrderedDict... but SortedDict is the way to go.
I was unfamiliar with its existence and API.
"""
from sortedcontainers import SortedDict
class StockPrice:
    def __init__(self):
        self.timestamp_to_price = SortedDict()
        self.price_to_timestamps = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamp_to_price:
            prev_val = self.timestamp_to_price[timestamp]
            self.price_to_timestamps[prev_val].remove(timestamp)
            if len(self.price_to_timestamps[prev_val]) == 0:
                self.price_to_timestamps.pop(prev_val)
        if price not in self.price_to_timestamps:
            self.price_to_timestamps[price] = set()
        self.price_to_timestamps[price].add(timestamp)
        self.timestamp_to_price[timestamp] = price

    def current(self) -> int:
        return self.timestamp_to_price.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.price_to_timestamps.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.price_to_timestamps.peekitem(0)[0]
