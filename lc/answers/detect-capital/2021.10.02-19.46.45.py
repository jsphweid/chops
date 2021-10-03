class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = []
        for i in range(len(word)):
            if word[i].isupper():
                capitals.append(i)
        return len(capitals) == len(word) or not len(capitals) or capitals == [0]