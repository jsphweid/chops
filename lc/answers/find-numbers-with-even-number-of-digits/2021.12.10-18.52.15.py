from math import log10
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([(int(log10(n)) + 1) % 2 == 0 for n in nums])