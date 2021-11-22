"""
[2,3,1,1,4]
end=4
depth=-1

depth=0
queue=[0]
    i=0 max_step=2
        j=1 queue=[1]
        j=2 queue=[1,2]
depth=1
queue=[1,2|]
    i=1 max_step=3
        j=1 queue=[2,2]
        j=2 queue=[2,2,3]
        j=3 queue=[2,2,3,4]
queue=[2|,2,3,4]
    i=2 max_step=1
        j=1 queue=[2,3,4,3]
depth=2
queue=[4,3,yada]
"""

from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1
        queue = deque([0])
        depth = -1
        seen = set()
        while queue:
            depth += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                if i in seen: continue
                seen.add(i)
                max_step = nums[i]
                if i == end: return depth
                for j in range(1, max_step + 1):
                    queue.append(i + j)