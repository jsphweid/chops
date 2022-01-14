def num_bouquets(bloomDay, day, k):
    acc, res = 0, 0
    for num in bloomDay:
        if day >= num:
            acc += 1
            if acc >= k:
                res += 1
                acc = 0
        else:
            acc = 0
    return res

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            day = (left + right) // 2
            if num_bouquets(bloomDay, day, k) >= m:
                right = day
            else:
                left = day + 1
        return left
