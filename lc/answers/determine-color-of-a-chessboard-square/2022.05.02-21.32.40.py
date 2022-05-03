class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l, n = coordinates[0], coordinates[1]
        return (l in "bdfh" and n in "1357") or (l in "aceg" and n in "2468")
