"""
===== Initial Thoughts =====
    **Input:** nums = [1,2,2]
    **Output:** [[],[1],[1,2],[1,2,2],[2],[2,2]]
[] [1] [1,2] [1,2,2] [2] [2,2] 

=== Brute Force Approach ===
[1,2,2]
00,01,02,10,

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[1,2,3]

res = {()}
recurse(0, []) new_path = [1]
    recurse(1, [1]) new_path = [1,2]
        recurse(2, [1,2])
    recurse(2, [1]) new_path = [1,3]
recurse(1, []) new_path = [2]
recurse(2, []) new_path = [3]
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = {()}
        def recurse(i, path=[]):
            new_path = path + [nums[i]]
            res.add(tuple(new_path))
            for j in range(i + 1, len(nums)):
                recurse(j, new_path)
        for i in range(len(nums)):
            recurse(i)
        return [list(item) for item in res]
