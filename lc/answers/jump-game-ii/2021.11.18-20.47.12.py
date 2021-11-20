"""
[3,3,3]
curr = 3,2,1

jump(nums=[2,3,1,1,4])

nums=[2,3,1,1,4] best=inf i=2 => 3
    min(inf, jump([1,1,4]))
    jump([1,1,4]) i=1 => 2
        best(inf, jump([1,4]))
            jump([1,4]) i=1 best => 1
    nums=[3,1,1,4] best inf

nums=[222,3,1,1,4]

original answer
from math import inf
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def dfs(jumps):
            if len(jumps) == 1: return 0
            if jumps[0] >= len(jumps) - 1: return 1

            best = inf
            i = min(jumps[0], len(jumps) - 1)
            while i > 0:
                new_jumps = jumps[i:]
                key = tuple(new_jumps)
                res = dp[key] if  key in dp else dfs(new_jumps)
                dp[key] = res
                best = min(best, res)
                i -= 1
            return best + 1
        return dfs(nums)


greedy
[2,3,1,1,4,3,2,1,1,4]
 0 1 2
   0 1 2 3
         0 1 2 3 4
                 0 1

[2,3,1,1,4,3,2,1,1,4]
N=10
while i<9
i=0 jumps=0
best=0 nxt=-1
    j=0 strength=2 best=2 nxt=0
    j=1 strength=4 best=4 nxt=1
    j=2 strength=3
i = 1 jumps=1
best=0 nxt=-1

[2,1]
 0 1 2
i=0 jumps=0 last=1
best=0 nxt=-1 range=[0:1]min(3,1)

[1,2,3]
   1
     1  2


[1,2]
last=1

[1,2]
   1

[1,2,3]
   1

[2,3,1]
   1 2

jumps = 1
[1,2,3]
 0 1

[9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]
 0 1 2 3 4 5 6 7 8 9
                   0 1 2 3 4 5

from math import inf
class Solution:
    def jump(self, nums: List[int]) -> int:
        i, jumps = 0, 0
        while i < len(nums) - 1:
            best, nxt = 0, -1
            for j in range(min(len(nums) - i, nums[i] + 1)):
                if j == 0 and ((i + nums[i]) >= (len(nums) - 1)):
                    return jumps + 1
                strength = nums[i + j] + j
                if strength >= best:
                    best = strength
                    nxt = i + j
            i = nxt
            jumps += 1
        return jumps

finally worked damn that was rough

studying the elegant version now...


[9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]
 0 1 2 3 4 5 6 7 8 9            l=0 r=9 

[8,99,9,4,8,1,6,1,5,6,2,1,7,9,0]
 0 1  2 3 4 5 6 7 8              l=0 r=8 nxt=100

[3,9,1,1,99,1,1,1,1,1,1,1,1,1,1]
 0 1 2 3         nxt=10


Finally working...

from math import inf
class Solution:
    def jump(self, nums: List[int]) -> int:
        i, jumps = 0, 0
        while i < len(nums) - 1:
            best, nxt = 0, -1
            for j in range(min(len(nums) - i, nums[i] + 1)):
                if j == 0 and ((i + nums[i]) >= (len(nums) - 1)):
                    return jumps + 1
                strength = nums[i + j] + j
                if strength >= best:
                    best = strength
                    nxt = i + j
            i = nxt
            jumps += 1
        return jumps

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        N = len(nums)
        def dfs(p):
            if p in dp: return dp[p]
            if p >= N - 1: return 0
            best = N
            i = min(nums[p], N - 1)
            while i > 0:
                best = min(best, dfs(i + p))
                dp[p] = best
                i -= 1
            res = best + 1
            dp[p] = res
            return res
        return dfs(0)
