def factorize(string: str):
    s = set([string])
    for i in range(1, (len(string) // 2) + 1):
        factor = string[:i]
        if (factor * (len(string) // i)) == string:
            s.add(factor)
    return s

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        f1 = factorize(str1)
        f2 = factorize(str2)
        common = f1.intersection(f2)
        longest = ""
        for item in list(common):
            if len(item) > len(longest):
                longest = item
        return longest