"""
rotating a number like that flips it upside down and reverses it essentially. 8 and 1
flip into themselves but 6 flips into 9 and 9 flips into 6. 0 -> 0

all other numbers I'm assuming have no strobogrammatic properties

69 -> 96
"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"1": "1", "6": "9", "9": "6", "8": "8", "0": "0"}
        transformed = []
        for n in num:
            if n not in mapping:
                return False
            transformed.append(mapping[n])
        return "".join(reversed(transformed)) == num

        