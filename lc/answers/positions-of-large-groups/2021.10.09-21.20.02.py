import re
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        return [[m.start(), m.end() - 1] for m in re.finditer(r"([a-z])\1{2,}", s)]
