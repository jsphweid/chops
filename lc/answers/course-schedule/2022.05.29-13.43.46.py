"""
FAILED on
5
[[1,4],[2,4],[3,1],[3,2]]
0 1 2 3 4
"""

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        checked = set()
        for course in list(range(numCourses)):
            if course in checked:
                continue
            stack = [(course, {course})]
            while stack:
                c, dupes = stack.pop()
                for child in adj[c]:
                    if child in dupes:
                        return False
                    if child not in checked:
                        checked.add(child)
                        stack.append((child, dupes | {child}))
        return True
