"""
===== Initial Thoughts =====
should be able to go over once and get counts
then we iterate over counts, we increment a global counter for any even number. We use a bool
to keep track of if an odd exists. Then we add num_evens + odd_exists

Actually, I just realized they want the length, (as opposed to what I don't know... :/)
This means we need the largest odd. And for evens, we need to add the actual counts, not increment

After failing many times because of a stupid mistake... I realized I'm not getting the problem...
you can keep more than 1 odd!!!!! if you have 3 3 3 3 counts for example, it's not 3, but 8...

~~Complexity Analysis
Time - O(2n)
Space - O(2n)
"""
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        for char in s: counts[char] += 1
        total = 0
        odd = False
        for count in counts.values():
            if count % 2 == 0: 
                total += count
            else:
                total += count - 1
                odd = True
        return total + odd

