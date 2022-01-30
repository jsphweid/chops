"""
===== Initial Thoughts =====
obviously the brute force is quite easy here.

the central part off this is trying to figure out how to do this efficiently.
how could we keep it ordered?

If we were doing this with sums, we could just pop the left item off and pop 
the right item on then divide by the window size.

The ordering is the tricky part here.

What if we had some ordered structure? Like a heap? SortedList

I just don't think is is very viable. Worst case for brute force is O(klogk) n-k times. With an
ordered list as linked list, add/subtract/find middle are all O(k) operations which is probably
not a big enough improvement over brute force. Actually, SortedList are all O(logk)... hmm. Maybe it's viable



=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

i = 2
[1,2,[3,4,5,6],7]


FAILED On 
[1,4,2,3]
4

"""

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res, lst, N = [], SortedList(nums[:k]), len(nums)
        for i in range(N - k + 1):
            
            if k & 1:
                res.append(lst[k // 2])
            else:
                l, r = lst[(k // 2) - 1], lst[k // 2]
                res.append((l + r) / 2)

            if i != N - k:  # has next
                lst.remove(nums[i])
                lst.add(nums[i + k])
        return res
