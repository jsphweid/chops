class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                counts[5] += 1
            elif bill == 10:
                counts[10] += 1
                if counts[5] < 1: return False
                counts[5] -= 1
            else:
                if counts[5] < 1 or counts[10] < 1:
                    if counts[5] < 3: return False
                    else: counts[5] -= 3
                else:
                    counts[5] -= 1
                    counts[10] -= 1
        return True