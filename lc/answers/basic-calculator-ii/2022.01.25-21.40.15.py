"""
===== Initial Thoughts =====
[3, "+", 5, "/", 2]

"""

class Solution:
    def calculate(self, s: str) -> int:
        items, num = [], 0
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if num or (i and s[i-1] == "0"):
                    items.append(num)
                    num = 0
                if char in "+-*/":
                    items.append(char)
        if num or (s[-1] == "0"):
            items.append(num)

            # now do two passes
        tmp, i = [], 0
        while i < len(items):
            if items[i] == "/":
                tmp.append(tmp.pop() // items[i+1])
                i += 1
            elif items[i] == "*":
                tmp.append(tmp.pop() * items[i+1])
                i += 1
            else:
                tmp.append(items[i])
            i += 1
        if len(tmp) == 1:
            return tmp[0]

        res, i = tmp[0], 1
        while i < len(tmp):
            if tmp[i] == "+":
                res += tmp[i+1]
            elif tmp[i] == "-":
                res -= tmp[i+1]
            i += 1
        return res



"""
res=5
[3, "+", 2, "-", 1]
[3, "+", 5, "/", 2]

"""