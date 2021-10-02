"""
===== Initial Thoughts =====
    **Input:** s = "5F3Z-2e-9-w", k = 4
    **Output:** "5F3Z-2E9W"

why do we just undash everything and upper case everything
"5F3Z-2e-9-w" -> "5F3Z2E9W"
then reverse that, iterating over the reversed thing
iterate in groups of k via math.ceil(len(str)/4)
each group, create a chunk str[i:i+k] and append to a list
join the list with "-"
reverse the whole thing

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
import math
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lst = [char.upper() for char in s if char != "-"]
        lst.reverse()
        chunks = []
        for i in range(math.ceil(len(lst) / k)):
            chunks.append("".join(lst[i * k: (i * k) + k]))
        final = "-".join(chunks)
        return final[::-1]