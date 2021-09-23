"""
===== Initial Thoughts =====
I can imagine an approach where you always increment and then go back and fix certain things
like
leetcode
10012340 -> then transition 12340 smoothly into 12210
But this method seems a little complex to code.
There might be another method if we allow ourselves to iterate over twice

Let's look for patterns:
leetcode
e's are at [1, 2, 7]
what if we used this to interpolate numbers in betwee
like [2, 7] -> 0, 1, 2, 2, 1, 0
or going further, a diff of
5 -> 1, 2, 2, 1, 0 min(1-0,5-1) min(2-0, 5-2) min(3-0, 5-3) min(4-0, 5-4) min
4 -> 1, 2, 1, 0
3 -> 1, 1, 0
2 -> 1, 0

leetcede
10011010

The hard part is what do you do before and after?

len=7
aaabaaa
3210123
[3]
list(range(1,3+1))[::-1]
list(range(1,3))

does it work if last one is the letter though?
len=7
aaaaaab
6543210
[6]
list(range(6+1))[::-1] 

ACTUALLY THIS IS DUMB why don't we just go over it three times?
once one way, the do it in reverse. increment up the second time (reset every time it hits).
third time will just be taking minimums.
loveleetcode
zzz010012340 (z is high number)
321010043210
loveleetcode
min...
321010012210... i.e. the answer 

=== Implemented Approach ===



~~Complexity Analysis
Time - O(n) (3n)
Space - O(n) (2n)
"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left = []
        right = []
        i = 10**5  # (above constraint)
        for char in s:
            if char == c:
                left.append(0)
                i = 1
            else:
                left.append(i)
                i += 1

        i = 10**5  # (above constraint)
        for char in s[::-1]:
            if char == c:
                right.append(0)
                i = 1
            else:
                right.append(i)
                i += 1
        right.reverse()
        return [min(a, b) for a, b in zip(left, right)]
