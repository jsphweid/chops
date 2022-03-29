"""
=== Brute Force Approach ===
convert to python list, then make BST

~~Complexity Analysis
Time - O(n)
Space - O(n)

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return self.makeBST(lst)

    def makeBST(self, lst):
        if not lst: return None
        mid = len(lst) // 2
        left = self.makeBST(lst[:mid])
        right = self.makeBST(lst[mid + 1:])
        return TreeNode(lst[mid], left, right)

=== Implemented Approach ===
Read some of the solutions and I really just need to do what I did above,
but instead of `lst`, just use the LL.

~~Complexity Analysis
Time - O(n)
Space - O(1)

1 2 3|4 5
        f
    s

1 2|3
    f
  s

[-10,-3,0,5,9]
            f
        s
"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        left, right = self.sortedListToBST(head), self.sortedListToBST(tmp.next)
        return TreeNode(tmp.val, left, right)
