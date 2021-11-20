from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = set("balloon")
        counts = defaultdict(int)
        for char in text:
            if char in s:
                counts[char] += 0.5 if (char == "l" or char == "o") else 1
        return int(min(counts.values())) if len(counts) == 5 else 0