"""
===== Initial Thoughts =====
very tedious way would be to have a dictionary contain the 8 different ways of winning and rules for
each new point on which of the 8 winning ways it contributes to. Then check the 8 winning ways, if there are
three items and they are all AAA or BBB, it's a winner, else ignore. If the moves list is less than 9,
return PENDING else DRAW.

~~Complexity Analysis
Time - O(n)
Space - O()

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
from collections import defaultdict
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        d = defaultdict(str)
        mapping = {
            (0, 0): ["ltb", "tlr", "ld"],
            (0, 1): ["mtb", "tlr"],
            (0, 2): ["rtb", "tlr", "rd"],
            (1, 0): ["ltb", "mlr"],
            (1, 1): ["mtb", "mlr", "ld", "rd"],
            (1, 2): ["rtb", "mlr"],
            (2, 0): ["ltb", "blr", "rd"],
            (2, 1): ["mtb", "blr"],
            (2, 2): ["rtb", "blr", "ld"],
        }
        for i in range(len(moves)):
            player = "A" if i % 2 == 0 else "B"
            buckets = mapping[tuple(moves[i])]
            for b in buckets:
                d[b] += player
                if len(d[b]) == 3:
                    if d[b] == "AAA": return "A"
                    if d[b] == "BBB": return "B"
        return "Draw" if len(moves) == 9 else "Pending"



