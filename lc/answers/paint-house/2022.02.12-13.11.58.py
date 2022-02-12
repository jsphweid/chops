"""
===== Initial Thoughts =====
brute force is obvious, 100^3 => 1,000,000 which means it'd probably be accepted just slow.
we could use backtracking to leave paths that will never beat the minimum

Actually it should be less than 1,000,000. Because from each point, you can only choose 2 on the 
subsequent houses. So it's more like 10,000.

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        stack = [(i, c, 0) for i, c in enumerate(costs[0])]
        seen, res = {}, float("inf")
        while stack:
            color, total, costs_i = stack.pop()
            if costs_i == len(costs) - 1:
                res = min(res, total)
            else:
                for nxt_color in range(3):
                    if nxt_color != color:
                        nxt_costs_i = costs_i + 1
                        nxt_cost = total + costs[nxt_costs_i][nxt_color]

                        key = (nxt_color, nxt_costs_i)
                        if key not in seen or nxt_cost < seen[key]:
                            seen[key] = nxt_cost
                            stack.append((nxt_color, nxt_cost, nxt_costs_i))
        return res

~~Complexity Analysis
Time - O(2^n)
Space - O(n)

not good...

Better idea would be to do a one-pass. Worked it out on the board and it's pretty simple.

[[17,2,17],[16,16,5],[14,3,19]]

The basic idea is to look ahead/behind and create a new list that is most optimal between
two sublists.

For example, looking at [17,2,17],[16,16,5]
The best combo total is 7.
Looking at the first 16, it's updated value is 16+2 or 16+17 (look behind)
Looking at the second 16, it's updated value is 16+17 or 16+17
Looking at the 5, it's updated value is 5+17 or 5+2.
We just choose the lowest one to continue on.
The graph problem is less optimal because it can branch out 
quite a bit in average/worst cases. There is no branching here
because it gets constrained to 3 every item in N.

~~Complexity Analysis
Time - O(N)
Space - O(1)
"""

class Solution:
    def minCost(self, c: List[List[int]]) -> int:
        for i in range(1, len(c)):
            c[i][0] = min(c[i][0] + c[i-1][1], c[i][0] + c[i-1][2])
            c[i][1] = min(c[i][1] + c[i-1][0], c[i][1] + c[i-1][2])
            c[i][2] = min(c[i][2] + c[i-1][0], c[i][2] + c[i-1][1])
        return min(c[-1])
