"""
quick plan would be to have a dictionary that contains lowercase letter -> count mapping from plate (ignoring numbers and spaces)
then for each word, we make a similar dictionary and ensure that it meets the criteria for the plate
if it meets, then we decide if it beats the best one -- we want the shortest
we return the best one (there must be 1)

1s3 PSt => {s: 2, p: 1, t: 1}

shortest = "steps"
step -> {s: 1, t: 1, e: 1, p: 1} - INVALID
steps -> {s: 2, t: 1, e: 1, p: 1} - VALID
stripe -> {s: 1} - INVALID
stepple -> {s: 1} INVALID

shortest = "pest"
1s3 456 => {s: 1}
looks -> {l: 1, o: 2, k: 1, s: 1}
pest -> {p: 1, e: 1, s: 1, t: 1}
"""

from collections import defaultdict

class Solution:
    def make_inventory(self, word: str) -> dict:
        # gets inventory of alpha lowercase char counts
        d = defaultdict(int)
        for char in word:
            if char.isalpha():
                d[char.lower()] += 1
        return d

    def meets_inventory(self, minimum: dict, in_dict: dict) -> bool:
        for char, count in minimum.items():
            if in_dict[char] < count:
                return False
        return True

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_inventory = self.make_inventory(licensePlate)
        shortest = None
        for word in words:
            inv = self.make_inventory(word)
            if self.meets_inventory(lp_inventory, inv):
                shortest = word if ((shortest is None) or (len(word) < len(shortest))) else shortest
        return shortest