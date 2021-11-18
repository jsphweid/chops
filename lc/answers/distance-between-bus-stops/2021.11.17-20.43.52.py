"""
sum(distance[start:destination])

[1,2,3,4]
[1,2,3,4,1,2,3,4]

[1,2,3,4,1,2,3,4] 0,3
[1,2,3] => 6
[3,4] => 4

[7,10,1,12,11,14,5,0]
7,2

"""

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        length = len(distance)
        distance *= 2
        l, r = (start, destination) if start < destination else (destination, start)
        clockwise = sum(distance[l: r])
        counter = sum(distance[r: l + length])
        return min(clockwise, counter)