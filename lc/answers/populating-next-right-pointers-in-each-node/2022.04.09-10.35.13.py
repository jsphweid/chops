class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        res = root
        while root and root.left:
            nxt = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                root = root.next
            root = nxt
        return res