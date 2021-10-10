"""
===== Initial Thoughts =====
easy with python
"""
import re
from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = re.findall(r"\-?\d+\/\d+", expression)
        result = str(sum([Fraction(int(n.split("/")[0]), int(n.split("/")[1])) for n in nums]))
        return result if '/' in result else f"{result}/1"