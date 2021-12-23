"""
===== Initial Thoughts =====
eat -> "a1e1t1" - key

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


["eat","tea","tan","ate","nat","bat"]

{"e": 1, "a": 1, "t": 1}
(("e", 1), ("a", 1), ("t", 1))
[("a", 1),("e", 1), ("t", 1)]
"a1e1t1"

""


from collections import defaultdict, Counter
def encode_str(string: str) -> str:
    res = ""
    for char, count in sorted(Counter(string).items()):
        res += f"{char}{count}"
    return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[encode_str(s)].append(s)
        return list(res.values())


but getting away from sorting...?
"""
from collections import defaultdict, Counter
def encode_str(string: str) -> tuple:
    lst = [0] * 26
    for char in string:
        lst[ord(char) - ord("a")] += 1
    return tuple(lst)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[encode_str(s)].append(s)
        return list(res.values())






