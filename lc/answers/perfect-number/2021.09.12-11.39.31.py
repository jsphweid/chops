"""
pretty simple, start at the square and move downward finding divisors and add them up

16
- 4x4
- 2x8
- 1x16
1 + 2 + 4 + (4?) + 8

it's not clear how squares are treated from the instructions... We'll assume no duplicates for first pass
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = set()
        start = int(num ** 0.5)
        while start > 0:
            if num % start == 0:
                divisors.add(start)
                divisors.add(num // start)
            start -= 1
        return (sum(divisors) - num) == num
        