"""
===== Initial Thoughts =====
n=5 k=3
123
124
125
134
135
145
234
235
245
345

[1,2,3,4,5]

res = []
path 1 [2,3,4,5] k=2

1 [2,3,4,5] k=2
1 2 [3,4,5] k=1
1 2 3

[1,2,3,4,5] k=3

~~Complexity Analysis
Time - 
Space - 

[1,2,3,4] k=2

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = list(range(1, n + 1))
        res = []
        self.recurse(lst, [], k, res)
        return res

    def recurse(self, lst, path, k, res):
        if len(path) == k:
            res.append(path)
        else:
            for i in range(len(lst)):
                self.recurse(lst[i + 1:], path + [lst[i]], k, res)



