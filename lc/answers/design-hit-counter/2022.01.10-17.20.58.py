"""
===== Initial Thoughts =====
hit 1
hit 2
hit 3
gethits 4 -> 3
hit 300
gethits 300 -> 4
gethits 301 -> 3

[1,2,3]
search for 4-300 = -296
it'll return 0. len list - 0 (3-0) => 3

probably should use bisect right? (since we don't want to include left...)
but how does this deal with duplicates?

[1,2,3,300] should return 4 if gethits(300)
bisect_right(0)->0
bisect_left(300)->3 (but that's bad... we want one over...)
should use both bisect_right
bisect_right(300)->4

if 301
bisect_right(1) -> 1
bisect_right(301) -> 4
returns 3... that's good

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
from bisect import bisect_right
class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return bisect_right(self.hits, timestamp) - bisect_right(self.hits, timestamp - 300)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)