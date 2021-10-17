"""
===== Initial Thoughts =====
if we order the dictionry and use regex replace with capture groups, it should work well...
"""
import re
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        joined = "|".join(sorted(dictionary))
        return re.sub(rf"\b({joined})\w+", r"\1", sentence)