"""
===== Initial Thoughts =====
arr = [1,6,1,2,500,42,3,0]
[0,1,1,2,3,6,42,500]
 1,0,1,1,3,36,458

k=1 res=>0
k=2 res=>1
k=3 res=>1
k=4 res=>1
k=5 res=>1
k=6 res=>1
k=7 res=>2
...
k=20 res=>41
# [0,1,1,1,1,1,2,2,2,3,3,4,5,5,6,36,39,40,41,41,42,458,494,497,498,499,499,500]

=== Brute Force Approach ===
do compare with each number in n^2 time and get distances.. then sort, then get k-1th one.

~~Complexity Analysis
Time - nlogn + n^2
Space - n^2

=== Implemented Approach ===
I know we need to use binary search but not sure now... (was reading that article)
So using the above example... If we guess 1... how would we get k=6

getting all the diffs isn't feasible. Is there a faster way to at least answer
"how many diffs" are below N?

had to look up the answer

the two pointer approach (slow/fast) is the way to go...
if we were to ask ourselves, how many diffs are less than 10?
the answer is 5+4+3+2+1 +3
[0,1,1,2,3,6,42,43,44]


~~Complexity Analysis
Time - 
Space - 

[1,1,3]
l=1 r=3 mid=2 s=0 f=0 res=3
l=1 r=2 mid=1 s=0 f=0 res=1
l=1 r=1 mid=0
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def num_pairs(limit):
            s, f, res = 0, 0, 0
            while s < len(nums) or f < len(nums):
                while f < len(nums) and nums[f] - nums[s] <= limit:
                    f += 1
                res += f - s - 1
                s += 1
            return res

        nums.sort()
        l, r = 0, max(nums)
        while l < r:
            mid = (l + r) // 2
            if num_pairs(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l










        