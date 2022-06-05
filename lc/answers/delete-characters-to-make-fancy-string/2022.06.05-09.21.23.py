class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_string = []
        for i in range(len(s)):
            if i < 2 or len({s[i], s[i-1], s[i-2]}) != 1:
                fancy_string.append(s[i])
        return "".join(fancy_string)
