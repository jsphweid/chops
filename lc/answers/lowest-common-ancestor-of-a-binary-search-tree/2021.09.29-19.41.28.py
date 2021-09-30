"""
===== Initial Thoughts =====


=== Brute Force Approach ===
For every node, see if the children are under it. If they are keep track of the depth. Then go deeper.
If the children node(s) also contain the two nodes/vals (lower depth), then replace the original winner.
If we reach a node that doesn't have both children, then you can stop pursuing that path.

~~Complexity Analysis
Time - Very bad, you can eliminate a lot, but it takes a lot of work to determine if the nodes even exist below
Space - 

Honestly, it's a BST. How can we leverage that?

Actually the search should be easy since it's BST. From their first example, p=2, q=8. First node is 6. That means 
there has to be one on the left and one on the right. That means it's the lowest actually. If the nums were 7,9 we
know we'd have to go right to get closer. Then we get to 8. Since 8 is between 7 and 9, we know to stop.

Another stopping condition is if we land on the number. For example, if the nums were 7,8, we'd land on the 8 and be done.

=== Implemented Approach ===
Traverse tree going in the direction of the nums. If it's between two nums then return that node. If we land on a node
that is equal to the value, then return that.

~~Complexity Analysis
Time - O(m) where m is tree depth
Space - O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller = p if p.val < q.val else q
        larger = p if smaller.val == q.val else q
        while (root is not p and root is not q) and not (smaller.val < root.val < larger.val):
            if root.left and p.val <= root.val:
                root = root.left
            else:
                root = root.right
        return root
