"""
===== Initial Thoughts =====
[[1,3],[1,4],[2,3],[2,4],[4,3]]
trust_map = {3:3, 4:2} potential_judges = {3,4} untrusted = {1,2,4}
{3}

n = 2, trust = [[1,2]]
counts={2:1}, untrusted={1}, trusted={2}

n = 3, trust = [[1,3],[2,3]]
counts={3:2}, untrusted={1,2}, trusted={3}

n = 3, trust = [[1,3],[2,3],[3,1]]
counts={3:2,1:1}, untrusted={1,2,3}, trusted={3,1}

n = 3, trust = [[1,2],[2,3]]
counts={2:1,3:1}, untrusted={1,2}, trusted={2,3}

n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
counts={3:3,4:2}, untrusted={1,2,4}, trusted={3,4}
"""
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1: return 1
        counts = defaultdict(int)
        trusted = set()
        untrusted = set()
        for left, right in trust:
            untrusted.add(left)
            trusted.add(right)
            counts[right] += 1
        for potential in (trusted - untrusted):
            if counts[potential] + 1 == n:
                return potential
        return -1