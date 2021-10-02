"""
===== Initial Thoughts =====
we could do a string split but that takes up memory space...
why don't we just count the number of spaces and add 1... only exception is "" which is 0

~~Complexity Analysis
Time - O(n)
Space - O(1)

Before I submit, I'm realizing we need to strip... can we do this without strip()?

and actually, what about something like "iasjdo   adi   asldf   " -> that should have 3, right?

what if we count non-space chars limiting continuous segments by 1
we iterate through the string, assigning a counter to 1 if non-space. Once we hit a space, we add the 1
at the end, we add whatever is on there
"""

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        current = 0
        for char in s:
            if char != " ":
                current = 1
            else:
                count += current
                current = 0
        return count + current