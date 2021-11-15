"""
8,8,7,6

seen={8,7,6}
uniques={7,6}

"""

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = set()
        uniques = set()
        for num in nums:
            if num in seen:
                if num in uniques:
                    uniques.remove(num)
            else:
                uniques.add(num)
                seen.add(num)
        return max(uniques) if len(uniques) else -1

