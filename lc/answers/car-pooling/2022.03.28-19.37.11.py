"""
===== Initial Thoughts =====
1, add 2
3, add 3
5, sub 2
7, sub 3

~~Complexity Analysis
Time - O(nlogn + n)
Space - O(n)
trips = [[2,1,5],[3,3,7]]
lst=[(1,2),(1,3),(-1,2),(-1,3)]
2+3+-2+-3
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for num_passengers, _from, _to in trips:
            lst.append((_to, -num_passengers))
            lst.append((_from, num_passengers))
        lst.sort()
        curr = 0
        for _, num in lst:
            curr += num
            if curr > capacity:
                return False
        return True
