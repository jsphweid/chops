from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        il = list(range(numRows - 1)) + list(range(numRows - 1, 0, -1))
        il = il * ceil(len(s) / len(il))
        output = [""] * numRows
        for i in range(len(s)):
            output[il[i]] += s[i]
        return "".join(output)