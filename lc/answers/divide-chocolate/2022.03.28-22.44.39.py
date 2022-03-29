class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def divides_enough(limit):
            slices = 0
            curr = 0
            for n in sweetness:
                curr += n
                if curr >= limit:
                    slices += 1
                    curr = 0
            return slices >= k + 1

        lo, hi = min(sweetness), sum(sweetness) + 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if divides_enough(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1  # [T, T, T, F, F, F, F, F]... we push towards first F, but want last T