"""
===== Initial Thoughts =====
add a 0...
[0,1,100,1,1,1,100,1,1,100,1]

look two steps ahead   
There are 4 possibilities
1 step + 1 step
1 step + 2 steps
2 steps + 1 step
2 steps + 2 steps
whichever has the lowest score, only take that first one or two step

then do that in a loop

find some condition to exit
if the second step is invalid

~~Complexity Analysis
Time - O(n)
Space - O(1)

[0,1,100,1,1,1,100,1,1,100,1]
i=3
last=9
total_cost=2

failed on [1,0,2,2]

I guess my solution just doesn't really work

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        i, last = 0, len(cost) - 2
        total_cost = 0
        while i < last:
            best_cost = float("inf")
            best_step = None
            for first_step, second_step in [(1, 1), (1, 2), (2, 1), (2, 2)]:
                # what's the lowest cost
                this_cost = cost[i + first_step]
                if i + first_step < last:
                    # only add the second step if it's possible to do so
                    this_cost += cost[i + first_step + second_step]
                if this_cost <= best_cost:  # tie breaks go to larger steps
                    best_cost = this_cost
                    best_step = first_step
            i += best_step
            total_cost += cost[i]
        return total_cost

WHY IS THIS PROBLEM SO HARD

The adding 0 at the beginning just doesn't quite make sense...
What if we just took that out at started at -1
Fails on the same problem... wait what

[1,0,2,2]

What if we added... 2 0's!

[0,0,10,15,20] would jump 1, then 2
[0,0,1,100,1,1,1,100,1,1,100,1] sould also work

wait it still fails... how!
[0,0,1,0,2,2] oh, i see, jeez. Same problem. 

Actually thinking through it with DP makes it a lot easier
just always look back and see what the minimum is and add it to current num
[1,100,2,3,3,103,4,5,104,6]
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

