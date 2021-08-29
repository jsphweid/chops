"""
a naive solution here should be fairly easy -- simply have a zero number as
a count, then add the right most bit (by anding with 1 and shifting in a loop)

There's probably a slick way to do this faster.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count

"""
failed because I was using notepad and forgot to indent everything by 4 spaces
"""