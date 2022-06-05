"""
~~Complexity Analysis
Time - O(kn)
Space - O(n)
"""

def sum_nums(single_letters: List[str]) -> List[str]:
    return list(str(sum([int(l) for l in single_letters])))

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        chars = []
        for c in s:
            chars.extend(list(str(ord(c) - ord("a") + 1)))
        for _ in range(k):
            chars = sum_nums(chars)
        return int("".join(chars))
