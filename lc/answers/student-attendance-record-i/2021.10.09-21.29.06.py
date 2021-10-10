import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        if len(re.findall(r"A", s)) > 1: return False
        if len(re.findall(r"L{3,}", s)): return False
        return True