def get_elements(root):
    if not root: return []
    return [root.val] + get_elements(root.left) + get_elements(root.right)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return sorted(get_elements(root1) + get_elements(root2))