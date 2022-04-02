"""
=== Implemented Approach ===
use a dict

~~Complexity Analysis
Time - O(n)
Space - O(n)

Hmmm... failed on "mgntdygtxrvxjnwksqhxuxtrv"
I got 14... it's supposed to be 18.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d, res = {}, -1
        for i, char in enumerate(s):
            if char in d:
                res = max(res, i - d[char] - 1)
            d[char] = i
        return res

I didn't understand the nuance of the problem. I assumed that a new char
would override the index if it already existed because you couldn't hop over
the same char but this is not the case.

With that in mind, all we have to do is not override it if it already exists...
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d, res = {}, -1
        for i, char in enumerate(s):
            if char in d:
                res = max(res, i - d[char] - 1)
            else:
                d[char] = i
        return res