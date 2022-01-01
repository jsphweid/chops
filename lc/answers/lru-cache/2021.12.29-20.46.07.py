"""
===== Initial Thoughts =====
lowest=4 highest=5
d={key3:3,key:4:4}
rank={4:key3,5:key4}
reverse={key:3:4,key4:5}


~~Complexity Analysis
Time - 
Space - 
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.lowest = 0
        self.highest = 0
        self.d = {}
        self.rank = {}
        self.reverse = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.highest += 1
            curr = self.reverse[key]
            self.reverse[key] = self.highest
            self.rank[self.highest] = key
            del self.rank[curr]
            return self.d[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.highest += 1
        if key in self.d:
            curr = self.reverse[key]
            self.reverse[key] = self.highest
            self.rank[self.highest] = key
            del self.rank[curr]
            self.d[key] = value
        else:
            self.reverse[key] = self.highest
            self.rank[self.highest] = key
            self.d[key] = value

        # handle if the LRU Cache is over size...
        if len(self.d) > self.capacity:
            while self.lowest not in self.rank:
                self.lowest += 1
            key_to_delete = self.rank[self.lowest]
            del self.d[key_to_delete]
            del self.reverse[key_to_delete]
            del self.rank[self.lowest]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)