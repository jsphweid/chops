"""
9,9,8,8,7,6,5,4,4
cantuse=True
previous=None can_use=True
num=9 previous=None can_use=True
num=9 previous=9 can_use=False
num=8 previous=9 can_use=True
num=8 previous=8 can_use=False
num=7 previous=8 can_use=True
num=6 previous=7 

9,9,8,8,7

1 can_use = True previous=1
"""

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        previous = None
        can_use = True
        for num in nums:
            if num == previous:
                can_use = False
            else:
                if can_use and previous != None:
                    return previous
                else:
                    can_use = True
            previous = num
        return previous if can_use else -1