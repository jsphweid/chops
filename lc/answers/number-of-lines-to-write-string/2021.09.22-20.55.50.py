"""
===== Initial Thoughts =====
Can be solved simply by storing letters -> widths in a dict then iterating over the string
each time string goes to the next "line" you can increment a counter +1. 

if limit is instead 10
so if a => 6
aaa we'll have 6,6,6 => [3, 6]
if a => 4 and aaaa, 4-4, 4-4 => [2, 8]
4,4,4,4... we'll accumulate 
4-4 (since 12 would be >10, we reset counter to 0, incremenet line counter by 1)

=== Implemented Approach ===
implementing the above, seems pretty straight-forward...

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        get_width = lambda char: widths[ord(char) - ord("a")]
        width_counter = 0
        line_counter = 1
        for char in s:
            width = get_width(char)
            if (width + width_counter) > 100:
                width_counter = width
                line_counter += 1
            else:
                width_counter += width
        return [line_counter, width_counter]
