"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

fn(5, [5])
    fn(8, [5, 8]) -> 13!
    fn(4, [5, 4])
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
fn(5, 9, [], 0)
    fn(4, 9, [], 0)

    fn(4, 9, [5], 5)
        fn()
    fn(8, 9, [], 0)
    fn(8, 9, [5], 5)
oops... has to be root to leaf... I thought too hard about this...
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []

        self.res = []
        self.recurse(root, targetSum, [], 0)
        return self.res

    def recurse(self, root, target, path, total):
        if total + root.val == target and not root.left and not root.right:
            self.res.append(path + [root.val])
        for node in [root.left, root.right]:
            if node:
                self.recurse(node, target, path + [root.val], total + root.val)
