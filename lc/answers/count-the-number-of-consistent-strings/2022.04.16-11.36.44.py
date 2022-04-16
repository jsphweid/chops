class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum([set(w) - set(allowed) == set() for w in words])