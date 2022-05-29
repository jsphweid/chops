def largest_group(lst):
    return max([len(s) for s in lst])

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros = largest_group(s.split("1"))
        ones = largest_group(s.split("0"))
        return ones > zeros