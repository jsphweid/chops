class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        streak = 1
        for num in flowerbed:
            if num == 0:
                streak += 1
            else:
                streak = 0

            if streak == 3:
                streak = 1
                total += 1
        return (total + (streak + 1 == 3)) >= n