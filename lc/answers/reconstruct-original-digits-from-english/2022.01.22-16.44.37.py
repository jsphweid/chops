"""
===== Initial Thoughts =====
very unique nums, 
zero - z
one - o (after original 5)
two - w
three - t (after original 5 + one)
four - u
five - f (after original 5 + one + three)
six - x
seven - v (after original 5 + one + three + five)
eight - g
nine - whatever is left

we need 3 pieces of information, num, letter, letters to subtract

tracing
owoztneoer
letter_counts = o:1, w:0, z:0, t:0, n:1, e:1, r:0
res_counts={0:1, 2:1}, res=""
z 0 0counts
occurences=1

pretty much an O(n) solution for time/space
"""
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        res_counts, res = {}, ""
        letter_counts = Counter(s)
        d = {
            "z": (0, Counter("zero")),
            "o": (1, Counter("one")),
            "w": (2, Counter("two")),
            "t": (3, Counter("three")),
            "u": (4, Counter("four")),
            "f": (5, Counter("five")),
            "x": (6, Counter("six")),
            "v": (7, Counter("seven")),
            "g": (8, Counter("eight")),
            "e": (9, Counter("nine"))
        }
        for char in "zwuxgotfve":
            num, counts = d[char]
            occurrences = letter_counts[char]
            res_counts[num] = occurrences

            for c, o in counts.items():
                letter_counts[c] -= o * occurrences

        for i in range(10):
            res += str(i) * res_counts[i]
        return res