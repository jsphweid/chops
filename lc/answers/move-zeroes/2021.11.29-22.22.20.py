"""
===== Initial Thoughts =====
can we swap?
[0,1,0,3,12]
[1,0,0,3,12]
NO

what about put to the end
[0,1,0,3,12]
[12,1,0,3,0] then swap? [1,12,0,3,0]
NO

what if we swapepd but did some look ahead
[0,1,0,3,12]
find next non-zero... 1 swap it
[1,0,0,3,12] find next non-zero... 3, swap it
[1,3,0,0,12] find next non-zero... 12, swap it!
[1,3,12,0,0] BINGO

tracing:
[0,1,0,3,12]
len=5
i=0 nums[i]=0
    j=0
    j=1
    swap done [1,0,0,3,12]
i=1 nums[i]=0
    j=1
    j=2
    j=3
    swap done [1,3,0,0,12]
i=2
    nums[i]=0
    j=2
    j=3
    j=4
    swap done [1,3,12,0,0]
i=3
    nums[i]=0
    j=3
    j=4

WOW. Somehow my tracing failed...
I forgot a break statement

THen FAILED AGAIN on [1]

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i
                while True:
                    j += 1
                    if j == len(nums): return
                    if nums[j] == 0: continue
                    nums[i] = nums[j]
                    nums[j] = 0
                    break
            i += 1

        