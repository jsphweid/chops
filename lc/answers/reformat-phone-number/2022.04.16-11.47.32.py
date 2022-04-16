"""
12345678
recurse("12345678")
    "123-" + recurse("45678")
        "456-" + recurse("78")
"""

class Solution:
    def reformatNumber(self, number: str) -> str:
        s = "".join([c for c in number if c.isdigit()])
        return self.recurse(s)

    def recurse(self, s):
        if len(s) == 4:
            return s[:2] + "-" + s[2:]
        if len(s) < 4:
            return s
        return s[:3] + "-" + self.recurse(s[3:])