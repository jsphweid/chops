import re
class Solution:
    def freqAlphabets(self, s: str) -> str:
        return "".join(chr(int(item[:2]) + ord("a") - 1) for item in re.findall("\d\d#|\d", s))