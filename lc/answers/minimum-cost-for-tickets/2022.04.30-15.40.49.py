"""
===== Initial Thoughts =====
let's try a bottom up
I couldn't think of it -- had to look it up...

[1,4,6,7,8,20]
[2,7,15]
[0,2,2,2,4,4,6,7,9,9,9,9,9,9,9,9,9,9,9,9,11]
[0,]
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        nxt_i = 0
        for i in range(1, len(dp)):
            if days[nxt_i] == i:
                nxt_i += 1
                dp[i] = min(dp[i - 1] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
