"""
===== Initial Thoughts =====
"042" -> 42
"+42" -> 42
"-42" -> -42
"42 and me" -> 42
"me and 42" -> 0
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        is_reading_digits = False
        digits = ""
        for char in s:
            if is_reading_digits:
                if char.isdigit():
                    digits += char
                else:
                    break
            else:
                if char == " ":
                    continue
                elif char == "-" or char.isdigit():
                    digits += char
                    is_reading_digits = True
                elif char == "+":
                    is_reading_digits = True
                else:
                    break
        num = int(digits) if digits != "" and digits != "-" else 0
        max_num = 2147483647
        min_num = -2147483648
        return max(min_num, num) if num < 0 else min(max_num, num)