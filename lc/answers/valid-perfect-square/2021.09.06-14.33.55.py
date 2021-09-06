class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq = num ** 0.5
        return sq == int(sq)