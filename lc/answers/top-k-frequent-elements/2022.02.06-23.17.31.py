"""
===== Initial Thoughts =====
if we use sorted containers it's probably something better than nlogn. like klogn?
"""
from collections import Counter, defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(list)
        for n, c in Counter(nums).items():
            d[c * -1].append(n)
        keys = list(d.keys())
        heapq.heapify(keys)
        res = []

        while k > 0:
            for n in d[heapq.heappop(keys)]:
                res.append(n)
                k -= 1

        return res
