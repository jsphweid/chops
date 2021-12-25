class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for word in words:
            for w in words:
                if word != w and word in w:
                    res.add(word)
        return list(res)