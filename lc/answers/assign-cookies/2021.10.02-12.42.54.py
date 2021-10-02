"""
=== Brute Force Approach ===
have a global count
iterate over s. for each item, find the largest value that is max the value of s[j]. if that value exists
remove the item and add 1 to global count.

thinking more...
we can eliminate the smallest excessive cookies thereby asserting that len of s can never be larger 
than len of g. But it can be smaller.

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        while len(g) and len(s):
            greediest_child = g.pop()
            largest_cookie = s[-1]
            if largest_cookie >= greediest_child:
                count += 1
                s.pop()
        return count
