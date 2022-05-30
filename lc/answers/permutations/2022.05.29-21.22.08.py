"""
===== Initial Thoughts =====
fn([1,2,3],[])
    fn([2,3],[1])
        fn([3],[1,2])
        fn([2],[1,3])
    fn([1,3],[2]) etc.
    fn([1,2],[3])

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.recurse(nums, [])
        return self.res
        
    def recurse(self, items, path):
        if items:
            for i in range(len(items)):
                self.recurse(items[:i] + items[i+1:], path + [items[i]])
        else:
            self.res.append(path)
