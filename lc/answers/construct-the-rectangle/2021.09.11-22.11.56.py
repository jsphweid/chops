"""
since one number will certainly be smaller than the sqrt of the area and the max size is 10000000...
then we could iterate through 3162 numbers (max) finding all other factors that are complimentary (I forgot
the proper math terms).
"""

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = int(area ** 0.5)
        while (area / i) != (area // i):
            i -= 1
        return [area // i, i]