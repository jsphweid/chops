"""
===== Initial Thoughts =====
I think a decent approach here is doing binary search to find the index of the x then adjust that
by some amount and return a range. Hard part here is what to do if there are duplicate numbers...
It doesn't mention that they are unique

[1,2,2,2,2,3,4,5] looking for 2
l=0 r=7 mid=3
l=0 r=3 mid=1
l=0 r=1 mid=0
l=1 r=1

For now I'm going to pretend like the numbers are unique...

Failed once, but the jury is still out on uniqueness..

Failed case #1 [-2,-1,1,2,3,4,5] k=7 x=3

My approach determines the best place to start is index 1, since found is 4 and 7//3 4-3=>1
Thing is, this number needs to be adjusted so window can capture entire group.
Can we always move it to the left by some number?

What about a more extreme example...?

[-5,-4,-3,-2,-1,1,2,3,4,5] k=7 x=3

I'm beginning to realize my approach doesn't make a lot of sense...
What if there are big gaps between numbers? My algorithm falls apart.

Really we need a way of prioritizing the numbers in some queue and we need to just pop off numbers
until we reach 7.

What if we found the index, then went left/right always choosing the next closest number?
The sort that at the end (probably can be done more strategically by insert 0 or append)
Hard part is handling cases like when you reach the end of the list.

I submitted but it was wrong...
[0,0,1,2,3,3,4,7,7,8] 3 5

Got most of them correct but this one failed.
The problem is that I'm forcing myself to start on an index which may lead me astray.
This binary search leads me to start on the first 7... but 4 is way closer to 5 than 7

To counter this, we could simply move l over to the left by 1 if that number exists and it's smaller.

l = l if (l == 0 or (abs(arr[l] - x) < abs(arr[l - 1] - x))) else l - 1

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        res = []
        l = l if (l == 0 or (abs(arr[l] - x) < abs(arr[l - 1] - x))) else l - 1
        l, r = l, l + 1
        while k > 0:
            k -= 1

            if l < 0:
                res.append(arr[r])
                r += 1
                continue

            if r == len(arr):
                res.append(arr[l])
                l -= 1
                continue

            a, b = arr[l], arr[r]
            if (abs(a-x) < abs(b-x)) or ((abs(a-x) == abs(b-x)) and (a<b)):
                res.append(arr[l] )
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        return sorted(res)