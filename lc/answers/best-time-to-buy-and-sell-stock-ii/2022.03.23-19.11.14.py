"""
=== Brute Force Approach ===
[7, 1, 5, 3, 6, 4]
 0 -6 -2 -4 -1 -3
    0  4  2  5  3
       0 -2  1 -1
          0  3  1
             0 -2
                0
this doesn't work

7 1 5 5 6 1 99
-6 4 0 1 -5 98

[1,2,3,4,5]
  1 1 1 1

[7, 1, 5, 3, 6, 4]
  -6  4 -2  3 -2

7  1  5  5  6  1  20
 -6 4  0  1  -5  19

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit