import re
class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        while (n - 1) > 0:
            output = self._compute_next(output)
            n -= 1
        return output

    def _compute_next(self, n: str) -> str:
        output = ""
        for group, digit in re.findall(r"((\d)\2*)", n):
            output += str(len(group)) + digit
        return output
