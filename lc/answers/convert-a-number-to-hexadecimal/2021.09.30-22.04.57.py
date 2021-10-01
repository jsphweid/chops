"""
===== Initial Thoughts =====
probably need to mask to keep negative numbers "bit-alive"

=== Implemented Approach ===
mask num with 0xffffffff
8 steps
  - shift 28-24-20-16 12-8-4-0
  - mask with 0b1111
  - look up num, add to str only if it's non-zero OR str has length

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def toHex(self, num: int) -> str:
        lookup = "0123456789abcdef"
        output = ""
        for i in range(8):
            shift = 28 - (i * 4)
            char = lookup[((0xffffffff & num) >> shift) & 0b1111]
            output += char if (output or char != "0" or shift == 0) else ""
        return output