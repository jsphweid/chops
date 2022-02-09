"""
===== Initial Thoughts =====
brute force is really obvious

=== Implemented Approach ===
[2,1,5,0,4,6]
2-1
1-1
5-2
0-1
4-2
6-3
the problem with looking at it this way is that there still requires searching.
For example, when we encounter 5, we know it's the second of some sequence.
But to know that, we have to scan all the 1's (i.e. [2,1]) see if they are less than 5
This is an n^2 approach -- better than n^3 but still not good enough most likely.

[2,1,5,0,1,2]
2-1
1-1
5-2
0-1
1-2
2-3

This is a better example probably.

I wrote this on the board and came up with a two sorted list solution

ones=[]
twos=[]

you have a new number. If insertion point of twos is 0. Then check insertion point of ones.
If it's 0 there, then put number in ones, else put number in twos.
Keep doing that. If insertion point of twos is one or greater, then return True.
ones=[2]
twos=[]
-----
ones=[1,2]
twos=[]
-----
ones=[1,2]
twos=[5]
-----
ones=[0,1,2]
twos=[5]
-----
ones=[0,1,2]
twos=[1,5]
-----
2 can go into twos at NOT the 0th position. Therefore return True.

~~Complexity Analysis
Time - O(nlogn)
Space - O(n)

What I realized though when writing this out. It's pretty redundant to keep all those numbers around.
For example... in the twos we have 5 for a while. Then when we got the 1, the 5 is irrelevant. Now every
item larger than a 1 will go out.
This means keeping lists is pointless. We can just store each as a number and update it with a minimum.

~~Complexity Analysis
Time - O(n)
Space - O(1)

from math import inf
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ones, twos = None, None
        for n in nums:
            if twos == None:
                if ones == None:
                    ones = n
                else:
                    if n > ones:
                        twos = n
                    else:
                        ones = min(ones, n)
            else:
                if n > twos:
                    return True
                else:
                    if n > ones:
                        twos = n
                    else:
                        ones = min(ones, n)
        return False

So that looks really ugly.. let's try to make it better
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ones, twos = float("inf"), float("inf")
        for n in nums:
            if n > twos:
                return True
            if n > ones:
                twos = n
            else:
                ones = min(ones, n)
        return False