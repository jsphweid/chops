from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        degrees = [0] * numCourses
        for i, j in prerequisites:
            adj[j].append(i)
            degrees[i] += 1
        stack = [i for i, d in enumerate(degrees) if d == 0]
        while stack:
            node = stack.pop()
            for child in adj[node]:
                degrees[child] -= 1
                if degrees[child] == 0:
                    stack.append(child)
        return sum(degrees) == 0
