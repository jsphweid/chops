"""
[1,2,3]
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
1 - 2,3
2 - 3

1
12
13
123

2
23

3

[1,2,3]

res=[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
recurse([1,2,3], [], res)
    recurse([2,3], [1], res)
        recurse([3], [1,2], res)
            recurse([], [1,2,3], res) -> DONE
        recurse([], [1,3], res) -> DONE
    recurse([3], [2], res)
        recurse([], [2,3], res) -> DONE
    recurse([], [3], res)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.recurse(nums, [], res)
        return res

    def recurse(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.recurse(nums[i + 1:], path + [nums[i]], res)

