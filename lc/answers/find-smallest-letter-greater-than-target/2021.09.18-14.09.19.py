"""
lets do the same but with binary search

this is interesting use of binary search. I know a very vanilla version of binary search but this
is challenging my understand of the algo.

say you have len=10 [0, 2, 4, 5, 5, 5, 8, 10, 11, 13] target 6
if you want to find the first num after 6...
0, 10 => i=5, v=5
5, 10 => i=7, v=10
5, 7  => i=6, v=8 - we have to stop here? why though, how do we know there is no 7?
probably because it's i=6 and we've already tried 5 and 7. 
maybe we're actually trying to find 7? (6 + 1)

what about len=9 [1, 1, 2, 2, 2, 2, 2, 2, 2] target 1
first num after 1...
but if we're trying to find 2 (1 + 1, value after 1), we find it immediately...
0, 9 => i=4, v=2
0, 4 => i=2, v=2
extra...
0, 2 => i=1, v=1 (then we know it's the last one)

len=18 [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] target 1
0,18 => i=9, v=2
0, 9 => i=4, v=1 -- we don't know 100% that this is last 4 value though
we could just start incrementing up from here in i though

let's read some answers...

interesting... bisect module

"""
import bisect
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect_right(letters, target)
        return letters[0] if len(letters) == i else letters[i]