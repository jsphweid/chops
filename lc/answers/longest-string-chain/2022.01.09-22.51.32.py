class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = {}
        for word in words:
            d[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in d:
                    d[word] = max(d[word], d[prev] + 1)
        return max(d.values())