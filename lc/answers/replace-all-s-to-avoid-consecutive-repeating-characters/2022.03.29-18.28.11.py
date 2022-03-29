# "jaqga?b"

def get_next(char1=None, char2=None):
    s = "abcd"
    for char in s:
        if char1 != char and char2 != char:
            return char

class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 1:
            return get_next() if s == "?" else s
        res = []
        for i in range(len(s)):
            if s[i] == "?":
                if i == 0 :
                    res.append(get_next(s[i + 1]))
                elif i == len(s) - 1:
                    res.append(get_next(res[i - 1]))
                else:
                    res.append(get_next(res[i - 1], s[i + 1]))
            else:
                res.append(s[i])
        return "".join(res)