"""
[0,2,1,-6,6,-7,9,1,2,0,1]

0 -- 2,3,-3,3,-4,5,6,8,8
0,2 -- 1,-5,1,-6,3,4,6,6
0,2,3 -- -6,0,-7,2,3 rest is 3

I think this fails in some cases though.. yolo

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        base_sum = 0
        for i in range(len(arr) - 2):
            base_sum += arr[i]
            middle_sum = 0
            for j in range(i + 1, len(arr) - 1):
                middle_sum += arr[j]
                if middle_sum == base_sum and sum(arr[j + 1:]) == base_sum:
                    return True
        return False

time limit exceeded... so brute force was correct...

how can we not add many of the same numbers up over and over...
[0,2,1,-6,6,-7,9,1,2,0,1]

0   2   1  -6   6  -7   9   1   2   0   1
0   2   3  -3   3  -4   5   6   8   8   9
3,6,9

{0: [0], 2: [1], 3: [2, 4], -3: [3], -4: [5], 5: [6], 6: [7], 8: [8, 9]}
last = 10


[3,3,6,5,-2,2,5,1,-9,4]
3   3   6   5  -2   2   5   1  -9   4
3   6   12  17  15  17  22  23  14  18
6 12 18
"""
from collections import defaultdict
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        last = 0

        # iterate once to build up sums
        total = 0
        last = 0
        sum_positions = defaultdict(list)
        for i, num in enumerate(arr):
            if i == (len(arr) - 1):
                last = total + num
            else:
                total += num
                sum_positions[total].append(i)

        # iterate again to get the result
        total = 0
        for i, num in enumerate(arr):
            total += num
            if total * 3 == last and (total * 2) in sum_positions and len([n for n in sum_positions[total * 2] if n > i]) > 0:
                return True
        return False


