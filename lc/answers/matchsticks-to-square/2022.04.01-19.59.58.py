"""
did this one with brian, failed it though. I thought about it for like 10-15 minutes and then 
implemented a solution I'm pretty sure doesn't work. And to confirm that, I'll redo 
the same solution here real quick.

failed on
[5,5,5,5,4,4,4,4,3,3,3,3]
[3,3,3,3,4,4,4,4,5,5,5,5] 48/4 == 12
basically my approach doesn't really work. It only passes 143 / 185 testcases.

from collections import deque
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side, remainder = divmod(sum(matchsticks), 4)
        if remainder: return False
        created = 0
        matchsticks.sort()
        queue = deque(matchsticks)
        while queue:
            if queue[-1] > side:
                return False
            if queue[-1] == side:
                created += 1
                queue.pop()
            elif len(queue) == 1:
                return False
            elif queue[0] + queue[-1] == side:
                created += 1
                queue.pop()
                queue.popleft()
            elif queue[0] + queue[-1] > side:
                return False
            else:
                l = queue.popleft()
                queue[0] += l
        return created == 4

given that there are only 15 matchsticks... I think DFS is the way to go.

side = 2
dfs([1,1,2,2,2], 0, 0)
    dfs([1,2,2,2], 1, 0)
        dfs([2,2,2], 2, 0)
            dfs([2,2,2], 0, 1)
                dfs([2,2], 2, 1)
                    dfs([2,2], 0, 2)
                        dfs([2], 2, 2)
                            dfs([2], 0, 3)
                                dfs([], 2, 3)

dfs 171 / 185 test cases passed. but ultimately TLE'ed

from collections import deque
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side, remainder = divmod(sum(matchsticks), 4)
        if remainder:
            return False

        def dfs(sticks, curr, created):
            if curr == side:
                if created + 1 == 4:
                    return not sticks
                if dfs(sticks, 0, created + 1):
                    return True
            for i in range(len(sticks)):
                if sticks[i] + curr <= side:
                    if dfs(sticks[:i] + sticks[i+1:], sticks[i] + curr, created):
                        return True
            return False
        return dfs(matchsticks, 0, 0)

I'm not immediately sure what can be cached.

Actually, if there is a list with a bunch of repeats, the same list will have been
seen many times because many are indistinguishable. But we need to tuplify
the list?
"""
from collections import deque
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side, remainder = divmod(sum(matchsticks), 4)
        if remainder:
            return False

        @cache
        def dfs(sticks, curr, created):
            if curr == side:
                if created + 1 == 4:
                    return not sticks
                if dfs(sticks, 0, created + 1):
                    return True
            for i in range(len(sticks)):
                if sticks[i] + curr <= side:
                    if dfs(sticks[:i] + sticks[i+1:], sticks[i] + curr, created):
                        return True
            return False
        return dfs(tuple(matchsticks), 0, 0)

