"""
===== Initial Thoughts =====
let's solve it with simulation

~~Complexity Analysis
Time - 
Space - 

res=19
remainder=3
numBottles=0
numExchange=4
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res, remainder = 0, 0
        while numBottles:
            res += numBottles
            numBottles, remainder = divmod(numBottles + remainder, numExchange)
        return res