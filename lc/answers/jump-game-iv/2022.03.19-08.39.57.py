"""
===== Initial Thoughts =====
seems like straight forward BFS
you can either go forward 1, back 1, or teleport
we need a dict that has indices of spots where we can teleport
finally we'll want a cache of indices we've seen. There'll be no point
in going over the same spots if we're BFSing

~~Complexity Analysis
Time - 
Space - 

[100,-23,-23,404,100,23,23,23,3,404]
100: [0,4]
-23: [1,2]
404: [3,9]
23: [5,6,7]
3: [8]
queue=[|]
i=0
seen={0}
end=9
res=0

TLE'ed but what if we popped off the lists... so it always does last first also makes it smaller
"""
from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        hops = defaultdict(list)
        for i, num in enumerate(arr):
            hops[num].append(i)
        queue = deque([0])
        seen = set()
        end = len(arr) - 1
        res = -1
        while queue:
            res += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                if i in seen:
                    continue
                seen.add(i)
                if i == end:
                    return res
                nxts = []
                while hops[arr[i]]:
                    nxts.append(hops[arr[i]].pop())
                nxts.append(i + 1)
                nxts.append(i - 1)
                for nxt in nxts:
                    if nxt not in seen and 0 <= nxt <= end:
                        queue.append(nxt)
