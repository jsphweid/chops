"""
===== Initial Thoughts =====
use regex to group the characters
not sure if gain much by using regex. will look at the answer after and see if they did it any differently.
"""
import re
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row_total = 0
        lines = 1
        for match in re.finditer(r"([a-z])\1*", s):
            i = ord(match.group(1)) - ord("a")
            count = match.end() - match.start()
            max_letter = ((100 - row_total) // widths[i]) * widths[i]
            ideal = widths[i] * count
            if ideal > max_letter: # we can't fit it
                lines += 1
                row_total = ideal - max_letter
            else:
                row_total += ideal
        return [lines, row_total]
