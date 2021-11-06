"""
===== Initial Thoughts =====
playing it out
[2,7,4,1,8,1]
[2,4,1,1,1]
[2,1,1,1]
[1,1,1]
[1]
1

[1]
1

=== Brute Force Approach ===
for each "round", find the two largest stones and "play the game". Playing the game means following the rules and leaving
what is left to be iterated on again in the future.

sorting
[2,7,4,1,8,1]
[16,7,4,2,1,1]
[8,4,2,1,1]

what if we didn't go in "order"... would we get the same answer
[2,7,4,1,8,1]
[5,4,1,8,1]
[1,1,8,1]
[1,7,1]
[1,6]
[5]

[2,7,4,1,8,1]
[8,7,4,2,1,1]
[4,2,1,1] - leftover
8-7=1
[4,2,1,1,1]
[1,1,1]
4-2=2
[1,1,1,2]
[2,1,1,1]
2-1=1
[1,1,1]
1-1=0
[1]

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len stones is at least 2
        while len(stones) > 1:
            # sort in reverse (largest to smallest) 
            stones.sort()
            # pop the top two, and append a result
            highest = stones.pop()
            second_highest = stones.pop()
            remainder = highest - second_highest
            if remainder:
                stones.append(remainder)
        
        # return the list of maybe one item as an item or as 0
        return stones[0] if len(stones) else 0
        