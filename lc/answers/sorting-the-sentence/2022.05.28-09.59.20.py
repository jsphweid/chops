class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        words = [(int(w[-1]), w[:-1]) for w in words]
        words.sort()
        words = [word for _, word in words]
        return " ".join(words)