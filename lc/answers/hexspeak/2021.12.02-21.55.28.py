class Solution:
    def toHexspeak(self, num: str) -> str:
        res = hex(int(num))[2:].replace("1", "I").replace("0", "O").upper()
        return res if set(res).issubset({'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}) else "ERROR"