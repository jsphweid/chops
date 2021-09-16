class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        num_planted = 0
        for i, space_filled in enumerate(flowerbed):
            if not space_filled:
                # if we can plant
                if ((i - 1 < 0) or not flowerbed[i - 1]) and ((i + 1 == len(flowerbed)) or not flowerbed[i + 1]):
                    flowerbed[i] = 1
                    num_planted += 1
                    if num_planted == n:
                        return True
        return False
        