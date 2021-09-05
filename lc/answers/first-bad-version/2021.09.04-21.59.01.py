"""
So the inefficient way to solve this would be to start at the latest and go down the list.

A less inefficient way would be to be to do a binary search. In a real life scenario I almost feel like binary
search wouldn't be the most effective as the most likely cases is that the "bad" one happened relatively recently.
Binary search would still be O(logn) though

the binary search would effectively be over a range 0...n

we should be able to do this without creating a list since that's just unnecessary overhead in this case (the version
sequence is linear)

We only have to plan a bit because our range is 1..n, not 0..n-1 like normal... although we could just adjust it
every time we called the API and gave back the correct answer eventually... honestly that's probably the easiest.
We would also need the feedback loop to incorporate it. In fact, the adding +1 is essentially just getting the value
from a 0..n-1 index since 1, 2, 3 => [1, 2, 3] => 0, 1, 2 index.

NEW / (old?) development... I just realized that this algo will find a bad version no doubt but we want the FIRST
bad version. [1, 2, 3, 4, 5, 6b, 7b, 8b, 9b] (where b is bad)... We want 6

we should be able to store the highest good version and use that to get closer...

that last good version is basically the left goal post. So the algorithm is probably only slightly different

The issue is around 1. If 1 is a bad version, we have to return 1. If we don't do this, the algo assumes 1 is good
because `last_good_version_index = 1`
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        # the algo assumes after this that 1 is good
        if isBadVersion(1):
            return 1

        last_good_version_index = 1
        high_bad_version_index = n

        while True:
            if last_good_version_index + 1 == high_bad_version_index:
                return high_bad_version_index
            midpoint = (last_good_version_index + high_bad_version_index) // 2
            if last_good_version_index == midpoint:  # i.e., it's stuck
                return last_good_version_index + 1  # i.e., it must be the next one
            if isBadVersion(midpoint):
                high_bad_version_index = midpoint
            else:
                last_good_version_index = midpoint
