"""
===== Initial Thoughts =====
[5, 0, 0]
snap -> 0
[6, 0, 0]


=== Brute Force Approach ===
store every snapshot in memory... very memory expensive

~~Complexity Analysis
Time - get O(1) snapshot O(n)
Space - O(n * max_snapshots)

=== Implemented Approach ===
just store differences
{0: {current: 0, snapshots: [(0, 5), (1, 6)]}, etc.}



~~Complexity Analysis
Time - 
Space - 
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[(-1, 0)] for i in range(length)]
        self.snapshot = 0

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.snapshot, val))

    def snap(self) -> int:
        snap = self.snapshot
        self.snapshot += 1
        return snap

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.data[index]
        if len(snapshots) == 1:
            return snapshots[0][1]
        l, r = 0, len(snapshots) - 1
        while l < r:
            mid = (l + r) // 2
            mid_snap_id = snapshots[mid][0]
            if mid_snap_id > snap_id:
                r = mid
            else:
                l = mid + 1
        if snapshots[l][0] == snap_id or l == 0:
            return snapshots[l][1]
        return snapshots[l][1] if snap_id > snapshots[l][0] else snapshots[l - 1][1]
"""
-1, 0 --- 2
l=0, r=1 mid=0
l=1

(0, 5), (1, 6), (3, 7), (4, 2), (90, 0)
5
l=0 r=4 mid=2
l=3 r=4 mid=3
l=4 r=4 

[(0, 5)]

,"snap","get"]
[,[],[0,3]]

{0: {current: 12, snaps: [(0,0), (1,0), (2,4), (3,12)]}}
get(0,1) -> 0
set(0,12)
get(0,1)
snap()
get(0,3)


["snap"]
[[0,2],[]]

{
    0: {curr: 16, snaps: [(0, 0), (1, 16)]}, 
    1: {curr: 5, snaps: [(0, 5)]}, 
    2: {curr: 5, snaps: [(0, 0), (2, 15)]},
    3: {curr: 0, snaps: [(0, 0)]},
}

["set","get","set","get","set"]
[[1,8],[1,0],[0,20],[0,0],[0,7]]
[null,0,null,0,null]

{
    0: {curr: 0, snaps: [(-1, 0)]}, 
    1: {curr: 8, snaps: [(-1, 0)]}, 
}

["get","snap","snap","get"]
[[0,2],[],[],[0,0]]
2
[(-1, 0),(0,15)]

"""



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)