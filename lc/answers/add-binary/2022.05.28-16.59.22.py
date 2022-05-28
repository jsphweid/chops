"""
===== Initial Thoughts =====
easy way is just to use python methods

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

or just write it all out
rem="1"
res=["1", "0", "1", "0"]
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        remainder = "0"
        res = []
        while a or b:
            aa = a.pop() if a else "0"
            bb = b.pop() if b else "0"
            strs = remainder + aa + bb
            ones = strs.count("1")
            remainder = "0"
            if ones == 0:
                res.append("0")
            elif ones == 1:
                res.append("1")
            elif ones == 2:
                res.append("0")
                remainder = "1"
            elif ones == 3:
                res.append("1")
                remainder = "1"
        res = reversed(res)
        res = "".join(res)
        return remainder + res if remainder == "1" else res
