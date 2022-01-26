"""
my first solution... didn't realize they were binary search trees...

def get_elements(root):
    if not root: return []
    return [root.val] + get_elements(root.left) + get_elements(root.right)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return sorted(get_elements(root1) + get_elements(root2))

hehe... :(

so inorder traversal is the way to go. But we have to basically interlace two different
trees together somehow
"""

def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        first, second = inorder(root1), inorder(root2)

        # now we just have to merge them...
        res = []
        while len(first) or len(second):
            if len(first) and len(second):
                to_use = first if first[-1] > second[-1] else second
                res.append(to_use.pop())
            elif len(first):
                res.append(first.pop())
            else:
                res.append(second.pop())
        return res[::-1]


