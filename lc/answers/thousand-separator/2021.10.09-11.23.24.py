"""
===== Initial Thoughts =====
use regex to split up into groups of 3... but we'll need to offset it by the remainder
for example: if str length is 8, remainder is 2... therefore
"12345678"[2:]
"12." + "345678"
"""
import re
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        if len(n_str) < 4: return n_str
        remainder = len(n_str) % 3
        sections = [n_str[:remainder]] if remainder else []
        sections += re.findall(".{3}", n_str[remainder:])
        return ".".join(sections)
