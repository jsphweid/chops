class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        N = len(nums)
        l, r = start, start
        while True:
            if nums[l] == target:
                return abs(l - start)
            if nums[r] == target:
                return abs(r - start)
            if r < N - 1: r += 1
            if l > 0: l -= 1
