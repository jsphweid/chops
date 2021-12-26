from math import inf
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        smallest, acc = inf, 0
        for num in nums:
            acc += num
            smallest = min(acc, smallest)
        return -smallest + 1 if smallest < 1 else 1
