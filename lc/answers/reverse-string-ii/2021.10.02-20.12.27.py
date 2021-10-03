"""
abcdefghij
k=3
10/3 round up => 4
0 - abcdefghij[0: 0 + 3] - cba
1 - abcdefghij[3: 3 + 3] - def
"""
import math
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        groups = []
        num_groups = math.ceil(len(s) / k)
        for i in range(num_groups):
            group = s[i * k: (i * k) + k]
            groups.append(group if i & 1 else group[::-1])
        return "".join(groups)
