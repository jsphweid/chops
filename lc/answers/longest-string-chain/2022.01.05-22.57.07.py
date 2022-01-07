"""
"bda"
"bdca"
===== Initial Thoughts =====
["a","b","za","ba","bca","bda","bdca"]

["xb", "xbc","cxbc", "pcxbc", "pcxbcf"]
    
=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

["a","b","ba","bca","bda","bdca"]
graph = [['a', 'b'], ['az', 'bd'] ['bde']]

bda bdca

["a","b","ba","bca","bda","bdca"]
lengths {1: ["a", "b"], 2: ["ba"], 3: ["bca", "bda"], 4: ["bdca"]}
[["a", "b"], ["ba"], ["bca", "bda"], ["bdca"]]

This was my original solution but it TLE'd

# a is_predecessor of b
def is_predecessor(a: str, b: str) -> bool:
    if len(a) + 1 != len(b):
        return False
    is_bad = False
    for i, char in enumerate(a):
        if char != b[i]:
            return a == b[:i] + b[i + 1:]
    return True

from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lengths, adj = defaultdict(list), defaultdict(set)
        for word in words:
            lengths[len(word)].append(word)
        graph = sorted(lengths.values(), key=lambda lst: len(lst[0]))
        
        if len(graph) == 1: return 1

        for i in range(1, len(graph)):
            us, vs = graph[i - 1], graph[i]
            for u in us:
                for v in vs:
                    if is_predecessor(u, v):
                        adj[u].add(v)

        def find_longest(node):
            if adj[node]:
                best = 0
                for child in adj[node]:
                    best = max(best, find_longest(child) + 1)
                return best
            else:
                return 1

        longest = 1
        for root in list(adj.keys()):
            longest = max(longest, find_longest(root))

        return longest
longest = 2
["a","b","ba","bca","bda","bdca"]
{"a": 1, "b": 1, "ba": 2, "bca": 3}
i=2 last=a, b
i=3 last=ca ba bc
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longest, dp = 1, {}
        for i, word in enumerate(sorted(words, key=len)):
            dp[word] = 1
            if i > 0:
                for j in range(len(word)):
                    last = word[:j] + word[j + 1:]
                    if last in dp:
                        dp[word] = max(dp[word], dp[last] + 1)
                        longest = max(longest, dp[word])
        return longest







