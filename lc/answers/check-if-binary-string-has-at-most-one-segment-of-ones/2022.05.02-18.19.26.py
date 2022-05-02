class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones_ended = False
        for char in s:
            if char == "0":
                ones_ended = True
            if char == "1" and ones_ended:
                return False
        return True
