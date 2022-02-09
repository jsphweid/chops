"""
===== Initial Thoughts =====
this seems similar to the problem I just did (increasing-triplet-subsequence)

I think the approach is the same but we need to sort first and make it more dynamic

[[1,2],[2,3],[3,4]]
  1      1     2

[[5,6],[6,8],[2,3],[1,7],[2,7],[3,4],[5,99]]
  1     1     1     1     1     1     1

[[5,6],[6,8],[2,3],[1,7],[2,7],[3,4],[5,99]]
[[1,7],[2,3],[2,7],[3,4],[5,6],[7,99],[8,9],[10,11]]
 1        1   1     1     2       3    3     4
[[2,3],[3,4],[5,6],[1,7],[2,7],[8,9],[10,11],[7,99]]
    1    1     2     1     1    3      4      

[[2,3],[3,4],[5,6],[2,7],[8,9],[10,11],[7,99]]

[[2,3],[3,4],[5,6],[1,7],[2,7],[8,9],[10,11],[7,99]]
  1     

r, quant
(9,3)

Hmm, I'm not exactly sure how to do it. I can think of an O(n^2) solution though

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        state = [1] * len(pairs)
        for i, (l, _) in enumerate(pairs):
            for j in range(i):
                r = pairs[j][1]
                if l > r:
                    state[i] = max(state[i], state[j] + 1)
        return max(state)
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        num_to_beat, res = -float("inf"), 0
        for l, r in pairs:
            if l > num_to_beat:
                num_to_beat = r
                res += 1
        return res
