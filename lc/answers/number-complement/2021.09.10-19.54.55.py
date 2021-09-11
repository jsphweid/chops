"""
~ doesn't behave like I'd want it to in python so we'll do this manually for now

you could ^ with -1 but that is basically the same as ~ apparently in python.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join(["1" if c == "0" else "0" for c in bin(num)[2:]]), 2)
