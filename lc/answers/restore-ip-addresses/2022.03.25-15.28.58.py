"""
===== Initial Thoughts =====
can't be over 255

101023

1 10 101
0 01(invalid)

~~Complexity Analysis
Time - 
Space - 

101023
recurse("101023", [])
    recurse("01023", ["1"])
        recurse("1023", ["1", "0"])
            recurse("023", ["1", "0", "1"])
                recurse("23", ["1", "0", "1", "0"]) -> DONE
            recurse("23", ["1", "0", "10"])
                recurse("3", ["1", "0", "10", "2"]) -> DONE
                recurse("", ["1", "0", "10", "23"]) -> GOOD
            recurse("3", ["1", "0", "102"])
    recurse("1023", ["10"])
    recurse("023", ["101"])


Failed on "25525511135" because i needed len(s) + 1, not -1.
I don't know why I messed that up. I should've thought about a case
where the s was just 1 char... Obviously we need a range(1, 2) to cover it
not range(1,0) or range(1,1).

"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.recurse(s, [])
        return self.res

    def recurse(self, s, path):
        if len(path) == 4:
            if s:
                return
            else:
                self.res.append(".".join(path))
        else:
            for i in range(1, min(4, len(s) + 1)):
                chunk = s[:i]
                if (chunk == "0" or chunk[0] != "0") and int(chunk) < 256:
                    self.recurse(s[i:], path + [chunk])
