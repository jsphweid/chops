"""
===== Initial Thoughts =====
just count it out

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[2,3,4,7,11], k = 5

i=4 j=10 k=0

[1,2,3,4], k = 2

i=4 j=5 k=2

[1], k=5

i=1 j=2 k=5
fast successful submission...

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 1
        while k and i < len(arr):
            if arr[i] == j:
                i += 1
            else:
                k -= 1
            j += 1
        return j + k - 1

can we jump further though?

[2,3,4,7,11], k = 5
i=3 j=5 k=4 at this moment, we can really jump more than 1.. 

[2,3,4,7,11], k = 5
i=3 j=7 k=2

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 1
        while k and i < len(arr):
            jump = 1
            if arr[i] == j:
                i += 1
            else:
                jump = min(k, arr[i] - j)
                k -= jump
            j += jump
        return j + k - 1


But since it's sorted there's no reason we can't use binary search.
It's a little tricky to imagine though.

[2,3,4,7,11], k = 5

k=1 -> 1
k=2 -> 5 i=3 v=7
k=3 -> 6 i=3 v=7
k=4 -> 8 i=4 v=11
k=5 -> 9 i=4 v=11


in this example, we know it crosses some line at index 4.
index expect actual off
0     1      2      1
1     2      3      1
2     3      4      1
3     4      7      3
4     5      11     6

and k is 5. But once we arrive at index 4 for binary search, how can we get the answer from there?
99 - 1 - 1
99 - (1 - 1)
7 - (3 - (2 - 1)) = 5
7 - 3 - 2 - 1 = 1

11 - (6 - (10 - 1))
arr = [2,3,4,7,11], k = 10
res = 15
4

k=7 12
k=8 13
k=9 14
k=10 15


[2]
1
l=0
off=1
is_below=1-1 <


got this right after 1 minor mistake... but how can I simplify it???
Yes, but my head hurts right now so I'm skipping 

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            off = arr[mid] - (mid + 1)
            if k <= off:
                r = mid
            else:
                l = mid + 1
        off = arr[l] - (l + 1)
        is_below = k - off <= 0
        return arr[l] + (k - off) - is_below

"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            off = arr[mid] - (mid + 1)
            if k <= off:
                r = mid
            else:
                l = mid + 1
        off = arr[l] - (l + 1)
        is_below = k - off <= 0
        return arr[l] + (k - off) - is_below
