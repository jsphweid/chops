class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        lst = []
        for n in num:
            if n not in mapping:
                return False
            lst.append(mapping[n])
        lst.reverse()
        return lst == list(num)
