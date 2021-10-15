"""
===== Initial Thoughts =====
the concept is simple here, but it's tricky to think about doing it efficiently
let's go with the brute force at first

=== Brute Force Approach ===
try putting a 1 at each 0 and for each time find the max number of continuous 
zeros. That is the number we're trying to minimize.

I wonder if we can do something DP related here
[1,0,0,0,1,0,1] - current
[1,1,0,0,1,0,1] -> 2 (index 1)
[1,0,1,0,1,0,1] -> 1 (index 2)
[1,0,0,1,1,0,1] -> 2 (index 3)
[1,0,0,0,1,1,1] -> 3 (index 5)

~~Complexity Analysis
Time - O(n^2)
Space - we only have to store the min. If the next answer beats the min,
then overwrite it.

So if we go with the brute force + caching, how would we do that?

The repition in counting comes from counting 0s from each sliced index.
Over and over and over again. If we're moving 1 over, then the most our count
can change is 2 (1 on each side), I think...

0 - [:0] + [1:] => 3 max(0, 3) (invalid because 1)
1 - [:1] + [2:] => 2 max(0, 2)
2 - [:2] + [3:] => 1 max(1, 1)
3 - [:3] + [4:] => 2 max(2, 1)
4 - [:4] + [5:] => 3 max(3, 1) (invalid because 1)
5 - [:5] + [6:] => 3 max(3, 0)
6 - [:6] + [7:] => 3 max(3, 0) (invalid because 1)

hang on, I'm not thinking about what can be cached. It's really hard to think
about the biggest groups that can be cached. For example, if I know that [1:]
is maxed at 3 (first step), how do I know where the group of 3 is. Is the next
i in the group of 3? or is it somewhere else? Seems not impossible but difficult
to cache...

I don't think I'm thinking clearly here. 

Actually, this should be much simpler. If we iterate once through, we can
keep track of open spaces to the left. But when we come across a 1, we have to
divide that number by //2 I think.

So with the above example [1,0,0,0,1,0,1]
We encounter a 0. We begin the streak
index 1 is 1 streak (starts)
index 2 is 2 streak
index 3 is 3 streak
index 4 breaks it... 3 - 1 == math.ceil(2/2) => 1 (that's the closest person)
but how do we record the index? result fo math.ceil + 1?

last streak end + max half?

the biggest streak is always going to be the winner. finding the index
is as simple as the last 1 + half biggest streak.



=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[1,0,0,0,1,0,1] - current

index 0 => biggest_streak=0, mid=0, streak=0, last_one=0
index 1 => biggest_streak=0, mid=0, streak=1, last_one=0
index 2 => biggest_streak=0, mid=0, streak=2, last_one=0
index 3 => biggest_streak=0, mid=0, streak=3, last_one=0
index 4 => biggest_streak=3, mid=2, streak=0, last_one=4
index 5 => biggest_streak=3, mid=2, streak=1, last_one=4
index 6 => biggest_streak=3, mid=2, streak=0, last_one=6

[1,0,0,0] - current
index 0 => biggest_streak=0, mid=0, streak=0, last_one=0
index 1 => biggest_streak=0, mid=0, streak=1, last_one=0
index 2 => biggest_streak=0, mid=0, streak=2, last_one=0
index 3 => biggest_streak=0, mid=0, streak=3, last_one=0

[0,1] - current
index 0 => biggest_streak=0, mid=0, streak=1, last_one=0
index 1 => biggest_streak=1, mid=1, streak=0, last_one=1


[0,0,1] - current
index 0 => biggest_streak=0, mid=0, streak=1, last_one=0
index 1 => biggest_streak=0, mid=0, streak=2, last_one=0
index 2 => biggest_streak=2, mid=1, streak=0, last_one=2

so after all this... we don't need to know the position, but simply the
distance???

Yikes... How did I misread that? the problem is literally called "Maximize 
Distance to Closest Person"


seems to be complicated by if it's at beginning or end

[0,0,0,1] => 3

normal cases
[1,0,0,0,0,0,0,1] => 3 (6/2)
[1,1,0,0,0,0,0,1] => 3 (5/2)
[1,1,1,0,0,0,0,1] => 2 (4/2)
[1,1,1,1,0,0,0,1] => 2 (3/2)
normal case is round up

[0,0,1], last_one gets moved to 2


[0,1,1,1,0,0,1,0,0]

[1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]


[0,0,0,0,1,0,1,0,0]

[0,0,0,0,0,0,0,1,0,0,0,0]

"""
import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        biggest_streak = 0
        distance = 0
        streak = 0
        last_one = -1
        first = None
        for i, seat in enumerate(seats):
            if seat == 0:
                streak += 1
            else:
                if first == None: first = streak
                if streak > biggest_streak:
                    biggest_streak = streak
                    distance = math.ceil(streak / 2)
                    last_one = i
                streak = 0
        return max(first, streak, distance)
                
        