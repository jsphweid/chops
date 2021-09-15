"""
this is tricky.

brute force would be to find every subsequence, eliminate all invalid ones, then find the one with
the max length and return. I'm not immediately sure how you would "find every subsequence" but it's 
obviously horribly inefficient for this problem.

I think there might be a clue in frequency in which numbers occur. From the first example, it seems
that we care about the most frequent items as they are likely to be 'involved' with the final result.
[1,3,2,2,5,2,3,7] yields {1: 1, 2: 3, 3: 2, 5: 1, 7: 1} when mapping number to its frequency of
occurence. If we order that from highest to lowest, we get the values 2, 3, 1, 5, 7. 

2 and 3 are 1 away so they are an eligable couple.

If we were to order these from top to bottom, then we'd clearly go with the FIRST eligable couple
else we'd default to 0. I think this makes sense.

The only possible trip up is the 1,5,7 issue. They are all 1. We'd probably need some secondary
sort on those because if they did happen to match (maybe it were 4, 1, 5 instead), we'd want
to at least match 4-5.

first non-bs error was failing on `[1,2,2,3,4,5,1,1,1,1]`
{1: 5, 2: 2, 3: 1, 4: 1, 5: 1}
sort should be [(1, 5), (2, 2), (5, 1), (4, 1), (3, 1)]

looks like I forgot to reverse...

then this failed... `[-3,-1,-1,-1,-3,-2]`
{-3: 2, -2: 1, -1: 3}
[(-1, 3), (-3, 2), (-2, 1)]
I see why it's failing... my algorithm might be incorrect. -1 and -2 are not next to each other

I'm starting to think I'm taking the wrong approach.
```
def findLHS(self, nums: List[int]) -> int:
    counts = defaultdict(int)
    for n in nums:
        counts[n] += 1
    if len(counts.keys()) > 1:
        # sort by frequency of occurence first, then sort by value secondly...
        sorted_entries = sorted(counts.items(), key=lambda e: (e[1], e[0]), reverse=True)
        for i in range(1, len(sorted_entries)):
            if abs(sorted_entries[i][0] - sorted_entries[i - 1][0]) == 1:
                good_nums = set([sorted_entries[i][0], sorted_entries[i - 1][0]])
                return len(list(filter(lambda n: n in good_nums, nums)))
    return 0

Actually what if we just kept the max of any two neighbors
```


"""
from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        if len(counts.keys()) > 1:
            # sort by frequency of occurence first, then sort by value secondly...
            sorted_entries = sorted(counts.items(), key=lambda e: e[0])
            winner = 0
            for i in range(1, len(sorted_entries)):
                if abs(sorted_entries[i][0] - sorted_entries[i - 1][0]) == 1:
                    winner = max(winner, sorted_entries[i][1] + sorted_entries[i - 1][1])
            return winner
        return 0