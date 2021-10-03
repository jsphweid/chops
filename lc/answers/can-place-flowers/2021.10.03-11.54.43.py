class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        streak = 0
        for num in [0] + flowerbed + [0]:
            if num == 0:
                streak += 1
            else:
                streak = 0

            if streak == 3:
                streak = 1
                total += 1
        return total >= n