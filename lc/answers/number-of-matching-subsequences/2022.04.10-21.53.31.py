"""
===== Initial Thoughts =====
we could make a crazy large trie that features every substring. 
lookup would be O(n)
But then we might as just have a set of every possibility and do
lookup on that (O(1)). Doesn't really seem feasible either way.

brute force would be to go through each word letter by letter.
You then check to see if that letter is in the remaining part of string
s, making the remaining part smaller each time.

There aren't a lot of words. But, each one can be very long.
But that means it can be pruned relatively quickly? A lot has
to go right for a 5000 long string to be in a 50000 string. It's
not likely we'll have to go through every letter. But it's all
about worst case.

s = string length (50000)
w = word length (5000)
N = list length (50)
Trie should be O(wN) time and O(s^2) space

this feels terrible.

=== Brute Force Approach ===
gotta implement it this way because I'm running out of time

~~Complexity Analysis
Time - O(swN)
Space - O(1)

s = "abcde", words = ["a","bb","acd","ace"]
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        @cache
        def get_next_i(start, char):
            for i in range(start, len(s)):
                if s[i] == char:
                    return i

        @cache
        def is_subsequence(w):
            last = -1
            for char in w:
                last = get_next_i(last + 1, char)
                if last == None:
                    return False
            return True

        res = 0
        for word in words:
            res += is_subsequence(word)
        return res