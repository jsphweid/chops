"""
~~Complexity Analysis
j is length of longest s
k is length of longest source
l is length of longest target
Time - O(j + nlogn + n(k + l))
Space - O(n)


s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
['a', 'b', 'c', 'd']
['e', 'e', 'e', 'c', 'd']

s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
lst = ['a', 'b', 'c', 'd']
start = 0, end = 1
lst[0:1] == ["a"]
['e', 'e', 'e', 'b', 'c', 'd']
offset=2
lst[4:6]
['e', 'e', 'e', 'b', 'f', 'f', 'f', 'f']


offset = -2
"vmossozp"
[3,5,1]
["kg","ggq","mo"]
["s","so","bfr"]


offset = 0
"vbfrssozp"
[3,5,1]
["kg","ggq","mo"]
["s","so","bfr"]


"""

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        offset = 0
        for index, source, target in sorted(zip(indices, sources, targets)):
            start, end = index + offset, index + len(source) + offset
            if s[start: end] == source:
                s = s[:start] + target + s[end:]
                offset += len(target) - len(source)
        return s















