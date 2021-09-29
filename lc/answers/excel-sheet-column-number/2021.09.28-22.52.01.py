"""
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        values = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lookup = {char: i for i, char in enumerate(values)}
        result = 0
        for i in range(len(columnTitle)):
            j = len(columnTitle) - i - 1
            result += ((26 ** j) * lookup[columnTitle[i]])
        return result