"""
===== Initial Thoughts =====
clearly binary search

~~Complexity Analysis
Time - O(log(n))
Space - O(1)

lets say 2 is bad
1 2 3 4 5 6 7 8
left=1 right=8 mid=4 4=bad go left
left=1 right=4 mid=2 2=bad go left
left=1 right=2 mid=1 1=good go right
left=2 END
return right, which is 2

lets say 7 is bad
1 2 3 4 5 6 7 8
left=1 right=8 mid=4 4=good go right
left=5 right=8 mid=6 6=good go right
left=6 right=8 mid=7 7=bad go left
left=6 right=7 mid=6 6=good go right
left=7 END
return right, which is 7
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right
                
            
        