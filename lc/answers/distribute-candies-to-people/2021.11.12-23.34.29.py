"""
===== Initial Thoughts =====
10
[5,2,3]

=== Brute Force Approach ===
iterate over a list over and over, filling it up with values

~~Complexity Analysis
Time - O(n) (where n is the number of candies)
Space - O(p) (where p is the number of people)

Input: candies = 7, num_people = 4
curr=1 res=[1,2,3,0]

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        curr = 1
        res = [0] * num_people
        while candies > 0:
            res[(curr - 1) % num_people] += min(candies, curr)
            candies -= curr
            curr += 1
        return res
