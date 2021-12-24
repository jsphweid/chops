from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for i in range(1, n + 1):
            d[sum(map(int, list(str(i))))] += 1
        lst = sorted(d.values())
        return lst.count(lst[-1])
