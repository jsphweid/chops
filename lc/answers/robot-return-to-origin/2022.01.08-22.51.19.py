class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vert, horz = 0, 0
        for move in moves:
            if move == "U":
                vert += 1
            elif move == "D":
                vert -= 1
            elif move == "L":
                horz -= 1
            elif move == "R":
                horz += 1
        return vert == 0 and horz == 0