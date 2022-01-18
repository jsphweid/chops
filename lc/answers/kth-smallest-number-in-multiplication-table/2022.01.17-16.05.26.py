"""
===== Initial Thoughts =====
hmm, ya "hard" seems appropriate

well I know that the approach is probably binary searching the result... 
but not sure how to put it all together

one row is like 1 2 3..., adding in another 1,2,2,3,4,6...

The numbers do make a pascal's triangle of sorts.

If we 'binary search the answer'... I'm not sure how we could get to a k from that.
we could find the number of ways to get that answer.
[1,2,2,3,3,4,6,6,9]
so guessing 3, we're trying to answer what is k is. given it's a 3x3, we can do 3x1 and 1x3.
that's 2 ways. + two ways to get 2. + 1 way to get 1. Which means 5. That's k so that's the answer.
But that's a lot of work for each search. There's gotta be a way to cut that back, right?
Otherwise it'd almost be more efficient to start from the bottom and just go up
1*1, 2*1 1*2

=== Brute Force Approach ===
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lst = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                lst.append(i*j)
        lst.sort()
        return lst[k-1]

~~Complexity Analysis
Time - if L is m*n... (L + L*log(L))
Space - O(L)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

l=1, r=9, m=5 total=6
l=1, r=5, m=

"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m*n
        while left < right:
            mid = (left + right) // 2
            # how many numbers are smaller or equal to mid
            total = 0
            for i in range(m):
                left_col = i + 1
                total += min((mid // left_col), n)
            if total < k:
                left = mid + 1
            else:
                right = mid
        return left


