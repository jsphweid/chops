"""
===== Initial Thoughts =====
let's use regex!

group everything together, then look at the divisibility of the lens each group.

000 111 000
3 3 3 -> 0 0 0 (divisibility)

000 11111 222
3 5 3 -> 0 2 0

we should just be able to filter out 0s and assert the only thing left is [2]
"""
import re
class Solution:
    def isDecomposable(self, s: str) -> bool:
        lens = [len(m.group(0)) for m in re.finditer(r"(\d)\1*", s)]
        return [l % 3 for l in lens if l % 3 != 0] == [2]
