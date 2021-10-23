import re
class Solution:
    def myAtoi(self, s: str) -> int:
        reading_digits = False
        digits = ""
        for char in s:
            if char.isdigit():
                if reading_digits:
                    digits += char
                else:
                    if char != "0":
                        digits += char
                        reading_digits = True
                    else:
                        reading_digits = True
            else:
                if reading_digits: 
                    break
                elif char == " ":
                    continue
                elif char == "+":
                    reading_digits = True
                elif char == "-":
                    digits += char
                    reading_digits = True
                else:
                    break
        if not digits or digits == "-": return 0
        num = int(digits)
        return max(-2147483648, num) if num < 0 else min(2147483647, num)

