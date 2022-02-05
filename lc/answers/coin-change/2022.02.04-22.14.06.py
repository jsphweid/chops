"""
===== Initial Thoughts =====
the amount is 10000 max
num coins is 12 or less
coin values themselves can be REALLY big

maybe this can be done by some greedy solution?

[1,2,5], amount = 11
clearly we want to use as many 5's as possible.

But we probably just can't go with the very first one that seems right or return -1

[5,4,1], amount = 8
the greedy approach would lead us to get 5+1+1+1, but the answer is really 4+4.

Maybe we just do the greedy approach starting with each coin?
For example, start with the 5, then do it with 4.
But what if we really need a 5 and then a 4?
5+4+4 = 13 is better than 5+5+1+1+1
we could do this as a graph search with backtracking. Still makes me think we could have
an explosion of possibilities. Let's try it. I've thought about it for too long already.

~~Complexity Analysis
Time - 
Space - 

[5,2,1], amount = 11

testing:
[5,4,1], amount = 13
queue=[(0,1,8),(1,1,9),(2,1)]
res=inf
coin_index=0 count=0 remaining=13

First solution was technically correct but TLE'ed

from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        queue, res = [(0, 0, amount)], inf
        while queue:
            coin_index, count, remaining = queue.pop()
            if remaining == 0:
                res = min(res, count)
            elif count < res and remaining > 0:
                for i in range(coin_index, len(coins)):
                    if remaining // coins[i]:
                        queue.append((i, count + 1, remaining - coins[i]))
        return -1 if res == inf else res

It's just a really expensive approach even with the backtracking.
I thought there was a possibility it wouldn't TLE but in hind sight it's pretty
obvious this is the wrong approach. Because it adds so many possibilities to the queue.
For example even a small example TLEs
[411,412,413,414,415,416,417,418,419,420,421,422]
9864
How many? I don't actually know how to calculate this. I know the tree in the above
example would be very very wide, but not too deep.
Hmm.. height worst case would be amount // smallest_num... width?

Let's rethink
[5,4,1] 13
5+5+1+1+1
4+4+4+1
5+4+4

divisor, remainder
13//5 = 2,3
13//4 = 3,1
13//1 = 13,0

we're essentially asking ourselves from this point... for the 5, since 3 is the remainder,
do we have a 3? The answer is no. Do we have an 8? a 13? (keep adding 5 back in).
The answer is no and no, although these questions are pointless because 5 is already the
highest.

What about 4? 13//4 = 3,1, do we have a 1? yes, but do we have a 5? also yes. 9? doesn't
matter because it's higher. But 5 is better because it allows us to trade off a number

Does it work here?
[5,4,1], amount = 8
8//5 = 1,3
8//4 = 2,0
8//1 = 8,0

So with the 4, we see we have a winner of 2. But 8//5 has a 1 so it has the potential
to be less than or equal to 2 if we find a home for the 3. (Well only equal to 2
in this case but the general theme is it could be less than if the disparity was bigger)

Maybe we need a priority queue actually?

The problem is that these basic examples are not letting us see the real difficulties.

[411,412,413,414,415,416,417,418,419,420,421,422]
9864//422 = 23,158
9864//421 = 23,181
9864//420 = 23,204
9864//419 = 23,227
9864//418 = 23,250
9864//417 = 23,273
9864//416 = 23,296
9864//415 = 23,319
9864//414 = 23,342
9864//413 = 23,365
9864//412 = 23,388
9864//411 = 24,0

[1,2,5], amount = 11
11//5 = 2,1
11//2 = 5,1
11//1 = 11,1

2,1 is in the lead so we check if there's a 1, there is, we push 3,0 to pqueue and pop next
since it's ",0" (and it was on top of pqueue) then we return.

13//5 = 2,3
13//4 = 3,1
13//1 = 13,0
revisiting this... we want to try to make 2,3 work. There is no 3. So we need to get
rid of a 2 making it 1,8. But then we have to check everything for an 8 (i.e. 5+1+1+1,
4+4, 1+1+1+1+etc.) which is really expensive. What if we used divmod though. Could reduce
a lot of redundancy but my intuition is that it would miss certain combinations. We'd
need a seen set too I think so we don't cross the same path again.

Let's just try something. If it doesn't work we'll look at the discussions.


import heapq
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pqueue, seen, coins = [], set(), set(coins)

        for coin in coins:
            d, r = divmod(amount, coin)
            heapq.heappush(pqueue, (d, [coin] * d, r))

        while pqueue:
            d, prev, r = heapq.heappop(pqueue)
            if (d, r) in seen:
                continue
            seen.add((d, r))

            if r == 0:
                return d
            if r in coins:
                heapq.heappush(pqueue, (d+1, prev+[r], 0))
            else:
                if prev:
                    heapq.heappush(pqueue, (d-1, prev[:-1], r+prev[-1]))
                for coin in coins:
                    div, rem = divmod(r, coin)
                    heapq.heappush(pqueue, (d+div, prev+([coin]*div), rem))

        return -1

Ok, this approach is fundamentally incorrect because we can add and subtract coins but we
also early exit if we discover a 0 remainder. We can't assume that a 0 remainder means exit
because there's always the possibility that one with a lower priority gets subtracted and 
comes out ahead in the end. But then it becomes hard to determine if we can early exit. We
have to explore all possibilities I believe. And that takes away the entire advantage of 
the pqueue. Also, the above method uses tons of memory (it could be optimized but it feels
wrong). It does pass almost every test though.

One more thing to try. What if we just used our original solution with a seen set?

still tle but in console it runs in like 50ms hmm... Time to look in discussions.

Ok discussions talk about BFS and DP. Of course.

BFS makes more sense to me. We don't have to store number of coins and remainder together in seen
as we're going from bottom up strategically -- so we only need remainder. Anything after it
that seens that remainder is less optimal because we're using BFS.

bfs trace
coins = [1,2,5], amount = 11
num_coins=2 [5,,3,6,4,7] seen={1,2,5,3,6,4,7} etc. should work

RETRO:
I spent a while on this going down wrong paths. I came up with a TLE fairly quickly but failed to see the beauty
of DFS for some reason. Usually I get that a problem is DFS pretty fast but didn't here for whatever reason.
I got distracted by backtracking pretty early. I should've seen "fewest number of coins" and thought BFS.
"""

from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        queue, seen, num_coins = deque([0]), {0}, 0
        while queue:
            num_coins += 1
            for _ in range(len(queue)):
                total = queue.popleft()
                for coin in coins:
                    new_total = total + coin
                    if new_total == amount:
                        return num_coins
                    if new_total < amount:
                        if new_total not in seen:
                            seen.add(new_total)
                            queue.append(new_total)
        return -1