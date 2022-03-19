"""
===== Initial Thoughts =====
extend the ends with 10 and 01 and run one algorithm over everything
2 (0,0) => 0
3 (0,0,0) => 1
4 (0,0,0,0) => 1
5 (0,0,0,0,0) => 2
6 (0,0,0,0,0,0) => 2
7 (0,0,0,0,0,0,0) => 3
/2 round up, subtract 1

import math
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.insert(0, 1)
        flowerbed.append(0)
        flowerbed.append(1)
        placed = 0
        streak = 0
        for spot in flowerbed:
            if spot == 1:
                placed += max(0, math.ceil(streak / 2) - 1)
                if placed >= n:
                    return True
                streak = 0
            else:
                streak += 1
        return False

~~Complexity Analysis
Time - O(n) (2 O(n) operations + 1 loop over (O(n)))
Space - O(1)

=== Implemented Approach ===
n is better than 3n though
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        i, total = 0, 0
        while i < len(flowerbed):
            if not flowerbed[i]:
                left_clear = True if i == 0 else flowerbed[i - 1] == 0
                right_clear = True if i == len(flowerbed) - 1 else flowerbed[i + 1] == 0
                if left_clear and right_clear:
                    flowerbed[i] = 1
                    total += 1
                    if total >= n:
                        return True
                    i += 2
                    continue
            i += 1
        return False

