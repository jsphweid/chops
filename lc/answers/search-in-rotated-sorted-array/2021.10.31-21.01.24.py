"""
===== Initial Thoughts =====
never 'rotated' on 0

so it's like binary search but in a *possibly* rotated list?

obviously writing an O(n) solution is trivial. 

[4,5,6,7,0,1,2] target = 0
0,6 m=3 0<7 so we want left BUT 4-7 doesn't include, go other way
4,6 m=5 return

[7,8,9,10,12,14,15,1,2,3,4] target = 3
0,10 m=5 3<14, left... BUT 7-14 doesn't include target... so opposite
6,10 m=8 3>2, right AND target in 2-4...
9,10 m=9 return

len = 9
[8,9,0,1,2,3,5,6,7] target = 0
0,8 m=4 9>1, so right, but not in range so go left
0,5 m=2 0 found

[8,9,10,11,13,14,6,7] target = 6
len=8
0,7 m=3 6<11... should go left, but it's not in range

honestly... 1 range always makes sense and 1 does not, at least starting out...
why don't we just be explicit ?

[4,5,6,7,0,1,2] target=0
0,6 m=3
4,6 m=5

[4,5,6,7,0,1,2] target=3
0,6 m=3
4,6 m=5

[1,3] target=3
0,1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if target == nums[0] else -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            # from here, there are two ranges and at least one of them makes sense
            # since that's the case, we can check that range and potentially go
            # in that direction or we're just go the other way...
            if nums[l] <= nums[mid]:  # i.e. the range makes sense...
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return l if nums[l] == target else -1

