"""
===== Initial Thoughts =====
[2,5,6,0,0,1,2]
it's harder with duplicates because we don't immediately know if it's increasing or decreasing because it could
be surrounded by duplicates.

looking for 3
[2,5,6,0,0,1,2]
l=0 r=6 m=3

what if we find the point of rotation? can we do that in logn time?
start is 2, end is 2

we're trying to find the first point at which a number is less than or equal to the min of first and last
[5,1,2,3]
[5,6,7,3]
[1,2,3,4]

but that doesn't work here...
[3,4,1,2,3]
[T,F,T,T,T] binary search can't work effectively here
unless we look for strictly less than
[F,F,T,T,F] still doesn't really work

What if we just try to find the first number than is lower than the first?
[3,4,1,2,3,5,7]
The logic we need to add is making sure if we move left, if it's actually larger,
we still might need to move right instead.
In the above
we start at index 3 value 2. It's smaller so we try to get even smaller and go left
we go to index 1 value 4. Now that's actually larger than the last, 2, so we actually
need to move right even though it's larger than the index 0 value 3.

Once we find the point of rotation. We can do a normal binary search on whichever section is more appropriate.

~~Complexity Analysis
Time - O(logn)
Space - O(1)


testing
[3,4,1,2,3,5,7] should work
[4,4,4,4,4,4,4] should work

[1,2,3,4,5,5,8]

[5,1,2,3]
[5,6,7,3] l=0 r=3 m=1 | l=2 r=3 m=2 | l=3 r=3 m=3, result
[5,6,7,8] l is 3, two groups are [5,6,7] then [8] which is a little wrong but still would work
[3,3,3,3] l=0 r=3 m=1 | l=2 r=3 m=2 | 

Submitted but failed... Passed almost all of them...

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        num_to_beat = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < num_to_beat:
                num_to_beat = nums[mid]
                r = mid
            else:
                l = mid + 1

        l, r = (0, l-1) if nums[0] <= target <= nums[l-1] else (l, len(nums) - 1)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return nums[l] == target

failed on 
nums=[1,0,1,1,1] target=0
Oof, this breaks because it can't find the two ranges well enough.
since mid is 1, which isn't less, we immediately go right... but we should go left

we could change `if nums[mid] < num_to_beat` to `if nums[mid] <= num_to_beat`
but I think that might break others...

for example:
[5,5,1,2]

Maybe we could do one where we go left and the other where we go right. Just seems like a mess.

I better look at the discussions on this one.

Ok, so this problem is kinda BS because worst case is O(n).
If we accept O(n), then we can do some stuff.

I have righteously failed this problem.

There are lots of tricky cases is the main problem. My algorithm was just not robust enough to handle these.
[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
13

[2,2,2,3,2,2,2]
3

[1,0,1,1,1]
0

[1,2,3,4,5,5,8]

[5,1,2,3]  # right is sorted
[3,4,1,2,3,5,7]  # right is sorted

Time to rewrite based on a discussion answer. This really is possible in one loop.

[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] 
l=0 r=18 m=9 etc
l=0 r=15 m=7
l=0 r=14 m=7
l=0 r=13 m=6
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]: # the right is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else: # left side is sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return nums[l] == target

