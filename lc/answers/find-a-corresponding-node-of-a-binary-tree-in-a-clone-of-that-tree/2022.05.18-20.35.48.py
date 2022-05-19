"""
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if target.val == cloned.val:
            return cloned
        for node in [cloned.left, cloned.right]:
            if node:
                res = self.getTargetCopy(original, node, target)
                if res:
                    return res

let's do the follow up
"""

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        orig, clon = [original], [cloned]

        while orig and clon:
            o = orig.pop()
            c = clon.pop()
            if o == target:
                return c
            if o.left: 
                orig.append(o.left)
                clon.append(c.left)
            if o.right:
                orig.append(o.right)
                clon.append(c.right)
