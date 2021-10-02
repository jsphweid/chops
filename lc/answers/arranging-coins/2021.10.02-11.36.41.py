"""
===== Initial Thoughts =====
it's that one again...
I think last time I solved it with math but only after looking up the answer. It also took a day.
I remember binary search was an optional. Let's do that. But first I have to think through why that's necessary.

1
2
3
4
5

answers
1 -> 1 row
4 -> 2 rows
8 -> 3 rows
20 -> 5 rows

=== Brute Force Approach ===
start at bottom of the sequence 1-2-3-4-5-n
keep a count and add to it each counter
once that count goes over n, then return the count

~~Complexity Analysis
Time - O(n)
Space - O(1)

Honestly let's just try that

so I failed a few times because I wasn't handling edge cases like 0,1, but then I realized iterating through a
finite range is dumb because you're just asking for None answers unless you get the math correct. It'd be much simpler
to just use a while loop here
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
        while True:
            count += i
            if count > n: return i - 1
            i += 1
