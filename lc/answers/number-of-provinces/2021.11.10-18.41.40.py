"""
===== Initial Thoughts =====
input = [[1,1,0],[1,1,0],[0,0,1]]
seen={0} count=1
seen={0,1} count=1
seen={0,1,2} count=2

[[1,0,0],[0,1,0],[0,0,1]]


"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = [0] * len(isConnected) # [0, 0, 0]
        count = 0

        def explore(city: int):
            if seen[city]: return
            seen[city] = 1
            for i, is_connected in enumerate(isConnected[city]):
                if i != city and is_connected:
                    explore(i)

        for i in range(len(isConnected)):
            if not seen[i]:
                count += 1
                explore(i)

        return count