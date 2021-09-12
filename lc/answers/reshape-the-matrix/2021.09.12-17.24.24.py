"""
we need a mechanism to keep gathering numbers despite their structure. Then we can just funnel it into
the place it needs to be.

Actually these are matrices so they are always two dimensional, which makes it much simpler.

And we can probably return relatively quickly if it's a shape that won't match.

If it matches, we almost don't need to know the row after that because the column is the list
length and they are simply appended to a larger list and returned
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened = [item for row in mat for item in row]

        # exit early if incorrect shape (r*c != len(flattened_mat))
        if len(flattened) != (r * c):
            return mat

        # use `c` to partition up flattened list, putting everything in a container and return
        ret = []
        for i in range(r):
            ret.append(flattened[i * c: (i * c) + c])
        return ret