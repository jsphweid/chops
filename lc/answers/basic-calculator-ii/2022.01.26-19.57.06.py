"""
===== Initial Thoughts =====
redoing this problem -- I read stefan p's answer and it makes more sense to me.

Previously I had this idea of doing */ first then +-. This made for a lot of code duplication.
The deeper insight here is thinking of everything as a */ and the +- just affect the sign with the 
"""
import re
class Solution:
    def calculate(self, s: str) -> int:
        total = 0

        # it's like a normal split but the capture group 'includes' them in the output
        it = iter(re.split(r"([\+\-\*\/])", s))

        temp = int(next(it))

        for op in it:
            next_temp = int(next(it))

            if op in "+-":
                total += temp
                sign = 1 if op == "+" else -1
                temp = sign * next_temp
            else:
                if op == "*":
                    temp *= next_temp
                else:
                    # NOTE: using // here won't work, for example -3//2 => -2... not -1.
                    temp = int(temp / next_temp)
        return total + temp