import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eats_in_time(bananas_per_hour):
            hours = 0
            for num_bananas in piles:
                hours += math.ceil(num_bananas / bananas_per_hour)
            return hours <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if eats_in_time(mid):
                r = mid
            else:
                l = mid + 1
        return l