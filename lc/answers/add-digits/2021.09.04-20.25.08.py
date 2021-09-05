"""
recursive way could involve strings pretty easily... we can do the follow up later...

how could we do this without strings... let's worry about that later
"""

class Solution:
    def addDigits(self, num: int) -> int:
        return num if num < 10 else self.addDigits(sum(map(int, str(num))))
            