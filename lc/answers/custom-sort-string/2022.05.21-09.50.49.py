"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_to_i = {c: i for i, c in enumerate(order)}
        custom_sorted = sorted([(char_to_i.get(c, 26), c) for c in s])
        return "".join([c for _, c in custom_sorted])

I wonder if we can do in linear time...?

"cba"
"abcd"
{d: 1}
res=[c, b, a, d]
"""
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        res = []
        for char in order:
            count = counts[char]
            if char in counts:
                res.extend([char] * count)
                del counts[char]
        for char, count in counts.items():
            res.extend([char] * count)
        return "".join(res)
