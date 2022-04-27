"""
=== Brute Force Approach ===
brute force is easy... just have 3 for loops


~~Complexity Analysis
Time - O(n^3)
Space - O(1)

fails on [2,5,3,4,1]
253,254,251
234,231 +1
241
534,531 +1
541 +1
341

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating) - 2):
            for j in range(i+1, len(rating) - 1):
                for k in range(j+1, len(rating)):
                    res += rating[i] < rating[j] < rating[k]
                    res += rating[i] > rating[j] > rating[k]
        return res

=== Implemented Approach ===
what if we sort first but keep track of positions

rating = [2,5,3,4,1]
[(1,4),(2,0),(3,2),(4,3),(5,1)]

then you can prune...
but not if we want to go in both directions
actually at the end of the day, once you sort, you pretty much end up
with the same thing... only with their indices not values
[(1,4),(2,0),(3,2),(4,3),(5,1)]
becomes
[4,0,2,3,1]
and you're playing the same game again...

Let's simplify... what if we only wanted to go up?
[2,5,3,4,1]... we know their is only 1 answer going up
starting with 2, we have our first one
then 5 is a streak of 2 with num 2
then 3 is a streak of 2 with num 2
then 4 is a streak of 3 with num 2 and num 3, and streak of 2 with nums 2 and 3
then 1 is not a streak with anything
we only reached 1 streak of 3...

that's n^2 time to do that. This is better than n^3! But how do we code it?

each index needs to store how many streaks
[2,5,3,4,1]
[
    {2:0, 3:0},  # 2
    {2:1, 3:0},  # 5
    {2:1, 3:0},  # 3
    {2:2, 3:1},  # 4
    {2:0, 3:0},  # 1
]

we can just do the other side in reverse

let's try another example...
[1,2,3,4]
[
    {2:0, 3:0},  # 1
    {2:1, 3:0},  # 2
    {2:2, 3:1},  # 3
    {2:3, 3:3},  # 4
]

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

dp = [
2   (0,0),
5   (1,0),
3   (1,0),
4   (2,1),
1   (0,0),
]
res=1

dp = [
1   (0,0),
4   (1,0),
3   (1,0),
5   (2,0),
2   (0,0),
]

dp = [
    1   (0,0),
    2   (1,0),
    3   (2,1),
    4   (3,0),
]

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        def count(lst):
            dp = [(0, 0)] * N
            res = 0
            for i in range(N):
                for j in range(i - 1, -1, -1):
                    if lst[j] < lst[i]:
                        ll, rr = dp[j]
                        l, r = dp[i]
                        dp[i] = (l + ll + 1, r + ll + rr)
                res += dp[i][1]
            return res

        return count(rating) + count(rating[::-1])

I'm just not counting things correctly. I think I need to go to bed.

Ok, next day. I start with a better example
1 2 3 4 5 6
6 - 123 124 125 126 134 135 136 145 146 156
5 - 234 235 236 245 246 256
4 - 345 346 356
3 - 456
each streak increase by the prev + some incrementing number
+ all the previous

the + all the previous is where we can easily us DP

We just need to solve for an example like this too:
[1,4,3,5,2] 135 145
 1 1 1 1 1
   2 2 2 2
       2
       2
       3
       3
 {2: 1, 3: 0}
 {2: 3, 3: 2}

we just need some way to count...

[1,4,3,5,2,7]
145 147 135 137 157 127 457 357 => 8
1 4 3 5 2 7
-----------
1 1 1 1 1 1
  2 2 2 2 2
      3   3
      3   3
          4
          4
          3

[1,4,3,5,2,7]
[1,2,2,5,2,12] -> makes no sense

[1,4,3,5,2,7]
145 147 135 137 157 127 457 357 => 8
1 4 3 5 2 7
-----------
[
  1  {1: 1},
  4  {1: 1, 2: 1},
  3  {1: 1, 2: 1},
  5  {1: 1, 2: 3, 3: 2},
  2  {1: 1, 2: 1},
  7  {1: 1, 2: 5, 3: 4, 4: 1}, (3 counts as 4, 4 counts as 4)
]
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        def count(lst):
            dp = [0] * N
            res = 0
            for i in range(N):
                num_smaller = 0
                for j in range(i - 1, -1, -1):
                    if lst[j] < lst[i]:
                        num_smaller += 1
                        res += dp[j]
                dp[i] = num_smaller
            return res

        return count(rating) + count(rating[::-1])

