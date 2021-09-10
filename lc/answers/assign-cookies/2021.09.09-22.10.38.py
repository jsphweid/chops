class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        num_successes = 0
        while i < len(g) and j < len(s):
            greed = g[i]
            size = s[j]
            if size >= greed:
                num_successes += 1
                i += 1

            j += 1

        return num_successes
        