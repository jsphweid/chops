"""
[3,2,2,4,1,4], days = 3
[1,2,2,3,4,4]    4 (5 days)
i=5
acc=8
days=4

[1,2,2,3,4,4]    5 (4 days)
[1,2,2,3,4,4]    6 ( days)

"""

def try_size(weights, size):
    acc = days = 0
    for num in weights:
        acc += num
        if acc > size:
            days += 1
            acc = num
    return days + 1

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights.sort()
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if try_size(weights, mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left