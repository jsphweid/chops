from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([-1] + [k for k, v in Counter(arr).items() if k == v])