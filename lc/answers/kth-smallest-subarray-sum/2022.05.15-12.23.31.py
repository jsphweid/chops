"""
===== Initial Thoughts =====
this is a hard

=== Brute Force Approach ===
get all the sub array sums, order then, choose kth smallest one

[3,3,5,5], k = 7
[0,3,6,11,16]

3,3,5,5
6,8,10
11,13
16

numbers are all positive...
meaning sums only goes up
[2,1,3]
[0,2,3,6]

2 1 3
3 4
6

[1,1,7,1]
[0,1,2,9,10]

1 1 7 1
2 8 8
9 9
10


[1,1,1,99]
[0,1,2,3,102]

1 1 1 99
2 2 100
3 101
102

that only get us close. we can't know definitively which layer it is in.

~~Complexity Analysis
Time - n^2 + nlogn
Space - n

=== Implemented Approach ===
I didn't get this without reading the discussions unfortunately. And I'm a little
disappointed in myself because apparently the answer is to binary search the answer.

I see it now...

Input: nums = [3,3,5,5], k = 7
Output: 10

the lowest sum is the lowest number 3
the highest sum is all of the numbers (since they are all positive) 16
lo=3 hi=16

so I'd normally guess 9 first, but let's start with 7 because 9 is too close to the answer.
how many are less than 7
we go through the list and contract expand and use math
[3] is less than 7
[3,3] is less than 7
[3,3,5] is NOT less than 7
[3,5] is NOT less than 7
[5] is less than 7
[5,5] is NOT less than 7
[5] is less than 7

Might be tempting to say 4 were less than 7 but notice we didn't count the other 3
There are actually 5
When we count [3,3], we need to count more than 1. It's actually 3 for just [3,3], but we already
counted the first 3.

What if we were looking for less than 12
There are 8...
Let's try a process
3 -> 1
3 3 -> 3
3 3 5 -> 6
3 3 5 5 -> bad
3 5 5 -> bad
5 5 -> 3
5

How about we find 1, then 3, then 6. Once we encounter bad, we subtract 1 and start over
3 -> 1
3 3 -> 3
3 3 5 -> 6
3 3 5 5 -> bad !!! (subtract 1)
    5 -> 1
    5 5 -> 3

9 - 1 => 8

This feels like it doesn't work all the time...

I'm wasting so much time trying to find an elegant way to do this...
Looked in the discussions. It seems like just getting the distance at each
valid step works
example:
[3,3,5,5] looking for less than or equal to 8
 3       - 1
 3 3     - 2
 3 3 5   - 0 (because invalid)
   3 5   - 2
   3 5 5 - 0 (because invalid)
     5 5 - 0 (because invalid)
       5 - 1
         = 6!
Don't immediately know why distance sums up num subarrays as well.

lo=3 hi=16
[3,4,5,6,7,8,9,10,11,12,13,14,15,16]
[F,F,F,F,F,F,F,T, T, T, T, T, T, T ] k=7

lo=1 hi=3
[1,2,3,4,5,6]
[F,F,T,T,T,T]
guessing 4 should be true
so I really want, 'has at least'
because guessing 4 would get me 5, which is >= k (4)
then trying smaller...
        guessing 3 would get me 4, which is >= k (4)


~~Complexity Analysis
Time - O(nlogn)
Space - O(1)

[3,3,5,5] guess=12
i=3 total=6 streak=1 curr=5
"""
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def has_at_least_k(guess):
            total = j = curr = 0
            for i in range(len(nums)):
                curr += nums[i]
                while curr > guess:
                    curr -= nums[j]
                    j += 1
                total += i - j + 1
            return total >= k
        l, r = min(nums), sum(nums) + 1
        while l < r:
            mid = (l + r) // 2
            if has_at_least_k(mid):
                r = mid
            else:
                l = mid + 1
        return l


