"""
===== Initial Thoughts =====
maybe use graph?
226
2
22

406

2 (26) (6)
22 (6)

numDecodings("2031")
    numDecodings("031") -> 0
    numDecodings("31")
        numDecodings("3")
            numDecodings("") -> 1


iteration TLE'ed

class Solution:
    def numDecodings(self, s: str) -> int:
        stack, res = [s], 0
        while stack:
            curr = stack.pop()
            if curr == "":
                res += 1
            elif curr[0] == "0":
                continue
            else:
                stack.append(curr[1:])
                if len(curr) > 1 and int(curr[:2]) < 27:
                    stack.append(curr[2:])
        return res      

need to cache...

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def numDecodings(self, s: str, cache={}) -> int:
        if s in cache:
            return cache[s]
        if s == "":
            return 1
        elif s[0] == "0":
            return 0
        else:
            res = self.numDecodings(s[1:])
            if len(s) > 1 and int(s[:2]) < 27:
                res += self.numDecodings(s[2:])
            cache[s] = res
            return res
