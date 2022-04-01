"""
sum(4, 0) nxt=0+4
    sum(9, 4) nxt=49
        sum(5, 49) nxt=490 + 
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], acc=0) -> int:
        nxt = acc * 10 + root.val
        l, r = root.left, root.right
        if l or r:
            return sum([self.sumNumbers(n, nxt) for n in [l, r] if n])
        else:
            return nxt
