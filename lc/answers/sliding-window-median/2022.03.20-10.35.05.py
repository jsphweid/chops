"""
=== Brute Force Approach ===
brute force is to window over the list, ordering the inner group each time
then getting the middle value. Let's do that again

~~Complexity Analysis
N times, you must copy K items and sort them
Time - O(N(K + KlogK))
Space - O(N + K) (store an individual K list and the final res N)

=== Implemented Approach ===
I think it makes since to keep an ancillary struture, but the expensive
part is re-ordering almost all the same numbers over and over again

We could use a sorted container. I think I remember something about two 
heaps (min/max together). But I'll use the sorted container approach first.

from sortedcontainers import SortedList

def get_median_of_sorted(lst):
    N = len(lst)
    if N & 1:
        return lst[N // 2]
    else:
        return (lst[N // 2] + lst[(N // 2) - 1]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res, lst = [], SortedList()
        for i in range(len(nums)):
            lst.add(nums[i])
            if i >= k:
                lst.remove(nums[i - k])
            if i >= k - 1: # we have enough items in there
                res.append(get_median_of_sorted(lst))
        return res

~~Complexity Analysis
Time - nlogk
Space - k + n

nums = [1,3,-1,-3,5,3,6,7], k = 3

[-3,-1,1,3,5]

[-1,-3] (min heap)
[5,3,1] (max heap, use negatives)

we need a 3 and pop the 1

Hmm... maybe this doesn't work because we're not just dealing with min/max
we need to find an arbitrary number (from point of view of sorted structure)

So it can be done, but... 
That's a little outside what is necessary for me to know for now I believe.

"""

from sortedcontainers import SortedList

def get_median_of_sorted(lst):
    N = len(lst)
    if N & 1:
        return lst[N // 2]
    else:
        return (lst[N // 2] + lst[(N // 2) - 1]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res, lst = [], SortedList()
        for i in range(len(nums)):
            lst.add(nums[i])
            if i >= k:
                lst.remove(nums[i - k])
            if i >= k - 1: # we have enough items in there
                res.append(get_median_of_sorted(lst))
        return res