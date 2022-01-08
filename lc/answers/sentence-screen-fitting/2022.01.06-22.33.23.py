"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

hello---
world---

res = 1, i = 0
rows = 0, curr_col = 2

cols=3

["i","had","apple","pie"], rows = 4, cols = 5
res=0 i=2 rows=3 curr_col=-1

["a", "bcd", "e"] 3 6
res=0 i=2 rows=3 curr_col=4

brute force is a lot of work.. but what if it 
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        res, i, curr_col = 0, 0, cols
        while rows:
            while True:
                L = len(sentence[i])
                if L <= curr_col:  # it can fit
                    if i == len(sentence) - 1: # it's the last
                        res += 1
                        i = 0
                    else:
                        i += 1
                    curr_col -= (L + 1)
                else:
                    curr_col = cols
                    rows -= 1
                    break
        return res


optimized solution still doesn't work... 
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        res, i, curr_col, curr_rows, used = 0, 0, cols, rows, False
        while curr_rows:
            if i == 0 and curr_rows != rows and not used:
                # we've repeated ourselves... we can skip over a lot

                cycle_cost = rows - curr_rows
                cycles_left = curr_rows // cycle_cost

                res += res * cycles_left
                curr_rows %= cycle_cost
                used = True
                continue

            while True:
                L = len(sentence[i])
                if L <= curr_col:  # it can fit
                    if i == len(sentence) - 1: # it's the last
                        res += 1
                        i = 0
                    else:
                        i += 1
                    curr_col -= (L + 1)
                else:
                    curr_col = cols
                    curr_rows -= 1
                    break
        return res


looking up answer now...

So I had an idea early on where a similar problem could be solved with pure calculation.
If words could extend over the line breaks it'd be easy to calculate because line breaks
just don't mean anything at that point.

If they didn't matter then we could calculate a number. But since they do matter, the result
is that number but dialed back a bit. Every once in a while, at the end of the line, we have
to maybe cut a word off. So a good algorithm is to loop over the rows, advancing to the end
immediately and dialing back until we hit an empty space. 

sentence = ["i","had","apple","pie"], rows = 4, cols = 5
"i had apple pie "
4 rows 5 cols
len=16

4
num=22

["hello","world"]
"hello world " 12
rows=2 cols=8
num=14
"""

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s, num = " ".join(sentence) + " ", 0
        for i in range(rows):
            num += cols
            if s[num % len(s)] == " ":
                num += 1
                continue
            while s[num % len(s)] != " ":
                num -= 1
            num += 1
        return num // len(s)



