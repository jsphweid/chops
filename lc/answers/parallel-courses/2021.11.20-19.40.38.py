"""
===== Initial Thoughts =====
make adjaceny list, do dfs, check for loops

[[1,3],[2,3]]
{1:[3], 2:[3]}
dfs([1,2],{})
    longest = 0
    dfs([3],{1}) => 1
    dfs([3],{2}) => 1
    longest = 1

[[1,2],[2,3],[3,1]]
al = {1:[2],2:[3],3:[1]}
dfs([1,2,3],{})
    longest=0
    dfs([2],{1})
        dfs([3],{1,2})
    dfs([3],{2})
    dfs([1],{3})

dp={}
dfs([1,2],{})

"""
from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        al = defaultdict(set)
        for l, r in relations: al[l].add(r)
        dp = {}
        def dfs(courses, seen=set()) -> int:
            if len(courses):
                longest = 0
                for course in courses:
                    if course in seen: return -1
                    res = dp[course] if course in dp else dfs(al[course], seen | {course})
                    if res == -1: return -1
                    dp[course] = res
                    longest = max(longest, res)
                return longest + 1
            else:
                return 0

        return dfs(list(al.keys()))

