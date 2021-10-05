"""
=== Implemented Approach ===
iterate over once, keep track of last char and first time it arrived (was different)

don't forget the end
"""

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 2: return []
        groups = []
        last_start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if i - last_start >= 3: groups.append([last_start, i - 1])
                last_start = i
        if len(s) - last_start >= 3: groups.append([last_start, len(s) - 1])
        return groups