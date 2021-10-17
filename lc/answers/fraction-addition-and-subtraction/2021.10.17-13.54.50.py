from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = sum(Fraction(c) for c in findall(r"\-*\d+\/\d+", expression))
        return f"{result.numerator}/{result.denominator}"